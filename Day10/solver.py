import os
from typing import Callable, List
import requests


AOC_SESSION = os.environ['AOC_SESSION']


def get_data() -> List[str]:
    data : List[str] = requests.get('https://adventofcode.com/2021/day/10/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8').split('\n')[:-1]
    
    return data


def solve_q1(data: List[str]) -> List[List[str]]:
    total = 0
    helper = {'(': ')', '{': '}', '[': ']', '<': '>'}
    scores = {')': 3, '}': 1197, ']': 57, '>': 25137}
    incomplete: List[List[str]] = []
    for line in data:
        stack: List[str] = []
        broke = False

        for c in line:
            if c in helper.keys():
                stack.append(c)
            else:
                if helper[stack.pop()] != c:
                    total += scores[c]
                    broke = True
                    break

        if len(stack) > 0 and not broke:
            incomplete.append(stack)
    
    print(total)
    return incomplete
                

def solve_q2(incomplete: List[List[str]]):
    scores = {'(': 1, '{': 3, '[': 2, '<': 4}
    auto_complete_scored: List[int] = []
    for line in incomplete:
        current_score = 0
        for c in line[::-1]:
            current_score *= 5
            current_score += scores[c]
        auto_complete_scored.append(current_score)
    
    auto_complete_scored.sort()
    print(auto_complete_scored[len(auto_complete_scored) // 2])


if __name__ == '__main__':
    data = get_data()    
    incomplete = solve_q1(data)
    solve_q2(incomplete)
