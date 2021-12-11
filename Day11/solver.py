import os
from typing import List, Set, Tuple
from copy import deepcopy
import requests


AOC_SESSION = os.environ['AOC_SESSION']


def get_data() -> List[List[int]]:
    data : List[str] = requests.get('https://adventofcode.com/2021/day/11/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8').split('\n')[:-1]

    octopuses_map = [[int(x) for x in row] for row in data]

    return octopuses_map


def explode(local: List[List[int]], i: int, j: int, exploded: Set[Tuple[int, int]]):
    if (i, j) in exploded:
        return

    local[i][j] = 0
    exploded.add((i, j))

    from_row = -1 if i != 0 else 0
    to_row = 2 if i != len(local) - 1 else 1
    from_col = -1 if j != 0 else 0
    to_col = 2 if j != len(local[0]) - 1 else 1

    for row in range(from_row, to_row):
        for col in range(from_col, to_col):
            if (row, col) != (0, 0):
                if (i + row, j + col) not in exploded:
                    local[i + row][j + col] += 1
                if local[i + row][j + col] > 9:
                    explode(local, i + row, j + col, exploded)
    

def solve_q1(data: List[List[int]]):
    total = 0
    local = deepcopy(data)
    for _ in range(100):
        exploded: Set[Tuple[int, int]] = set()
        for i in range(len(local)):
            for j in range(len(local[0])):
                local[i][j] += 1
        
        for i in range(len(local)):
            for j in range(len(local[0])):
                if local[i][j] > 9:
                    explode(local, i, j, exploded)
        total += len(exploded)
                                
    print(total)


def solve_q2(data: List[List[int]]):
    gen = 0
    exploded: Set[Tuple[int, int]] = set()
    while len(exploded) != 100:
        gen += 1
        exploded: Set[Tuple[int, int]] = set()
        for i in range(len(data)):
            for j in range(len(data[0])):
                data[i][j] += 1
        
        for i in range(len(data)):
            for j in range(len(data[0])):
                if data[i][j] > 9:
                    explode(data, i, j, exploded)
    
    print(gen)


if __name__ == '__main__':
    data: List[List[int]] = get_data()    
    solve_q1(data)
    solve_q2(data)
