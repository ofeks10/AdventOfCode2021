import os
from typing import List, Tuple
from functools import reduce
from json import loads
import requests


AOC_SESSION = os.environ['AOC_SESSION']


import sys

class Node:
    def __init__(self, data, depth = 0):
        self.left = None
        self.right = None
        self.parent = None
        self.data = None
        self.depth = depth

        if type(data) is str:
            data = eval(data)
        if type(data) is int:
            self.data = data
        else:
            self.left = Node(data[0], depth + 1)
            self.right = Node(data[1], depth + 1)
            self.left.parent = self
            self.right.parent = self

    def isleaf(self):
        return (self.data is not None)

    def root(self):
        n = self
        while n.parent is not None:
            n = n.parent
        return n

    def leaves(self):
        if self.isleaf():
            return [self]
        else:
            ret = []
            if self.left is not None:
                ret += self.left.leaves()
            if self.right is not None:
                ret += self.right.leaves()
            return ret

    def ispair(self):
        return (
            self.left is not None and
            self.left.isleaf() and
            self.right is not None and
            self.right.isleaf()
        )

    def explode(self):
        leaves = self.root().leaves()
        if self.left.isleaf() and leaves.index(self.left) > 0:
            leaves[leaves.index(self.left) - 1].data += self.left.data
        if self.right.isleaf() and leaves.index(self.right) < (len(leaves) - 1):
            leaves[leaves.index(self.right) + 1].data += self.right.data
        self.left = None; self.right = None; self.data = 0

    def split(self):
        self.left = Node(self.data // 2, self.depth + 1)
        self.right = Node(self.data - (self.data // 2), self.depth + 1)
        self.left.parent = self
        self.right.parent = self
        self.data = None

    def reduce(self):
        def do_explode(n):
            nonlocal reducted
            if not reducted and n.left is not None: do_explode(n.left)
            if not reducted and n.ispair() and n.depth >= 4:
                n.explode()
                reducted = True
            if not reducted and n.right is not None: do_explode(n.right)
        def do_split(n):
            nonlocal reducted
            if not reducted and n.left is not None: do_split(n.left)
            if not reducted and n.isleaf() and n.data >= 10:
                n.split()
                reducted = True
            if not reducted and n.right is not None: do_split(n.right)

        while True:
            reducted = False
            prevt = Node(self.__repr__())
            do_explode(self)
            if not reducted: do_split(self)
            if prevt.__repr__() == self.__repr__():
                break

    def __add__(self, t):
        n = Node(f"[{self},{t}]")
        n.reduce()
        return n

    def magnitude(self):
        if self.isleaf():
            return self.data
        else:
            return 3*self.left.magnitude() + 2*self.right.magnitude()

    def __repr__(self):
        if self.isleaf():
            return f"{self.data}"
        else:
            return f"[{self.left},{self.right}]"

def process(content):
    lines = [l.strip() for l in content]
    total = Node(lines[0])
    total.reduce()
    for n in lines[1:]:
        t = Node(n)
        t.reduce()
        total += t
    return total.magnitude()

def get_data() -> List[int]:
    data : List[str] = requests.get('https://adventofcode.com/2021/day/18/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8').split('\n')[:-1]

    snails = list(map(loads, data))

    return snails


def solve_q1(data: List[int]):
    total = Node(data[0])
    total.reduce()
    for n in data[1:]:
        t = Node(n)
        t.reduce()
        total += t
    print(total.magnitude())


def solve_q2(data: List[int]):
    sums = []
    for l in range(len(data)):
        other_lines = data.copy()
        other_lines.pop(l)
        sums.append([])
        for o in other_lines:
            n = Node(data[l])
            n += Node(o)
            sums[l].append(n.magnitude())
    print(max([i for l in sums for i in l]))


if __name__ == '__main__':
    snails = get_data()    
    solve_q1(snails)
    solve_q2(snails)
