import os
from typing import Callable, List
import requests


AOC_SESSION = os.environ['AOC_SESSION']


def get_data() -> List[str]:
    data : List[str] = requests.get('https://adventofcode.com/2021/day/10/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8').split('\n')[:-1]
    
    # data = open('./Day10/example.in', 'r').read().split('\n')[:-1] 

    # print(data)

    return data


def solve_q1(data: List[str]) -> List[str]:
    total = 0
    helper = {'(': ')', '{': '}', '[': ']', '<': '>'}
    scores = {')': 3, '}': 1197, ']': 57, '>': 25137}
    incomplete: List[str] = []
    for line in data:
        stack: List[str] = []
        broke = False
        for c in line:
            if c in '({[<':
                stack.append(c)
            else:
                last = stack.pop()
                if helper[last] != c:
                    total += scores[c]
                    broke = True
                    break
        if len(stack) > 0 and not broke:
            incomplete.append(line)
    
    print(total)
    return incomplete
                

def solve_q2(incomplete: List[str]):
    helper = {'(': ')', '{': '}', '[': ']', '<': '>'}
    scores = {')': 1, '}': 3, ']': 2, '>': 4}
    auto_complete_scored: List[int] = []
    for line in incomplete:
        stack: List[str] = []
        for c in line:
            if c in '({[<':
                stack.append(c)
            else:
                last = stack.pop()
        # print(stack)
        current_score = 0
        while len(stack) > 0:
            last = stack.pop()
            current_score *= 5
            current_score += scores[helper[last]]
        auto_complete_scored.append(current_score)
        # print(auto_complete_scored)
    
    auto_complete_scored.sort()
    print(auto_complete_scored)
    print(auto_complete_scored[len(auto_complete_scored) // 2])


if __name__ == '__main__':
    data = get_data()    
    incomplete = solve_q1(data)
    solve_q2(incomplete)
