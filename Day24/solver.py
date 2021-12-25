import os
from typing import Dict, List, Tuple
import requests


AOC_SESSION = os.environ['AOC_SESSION']


def get_data() -> List[str]:
    data : List[str] = requests.get('https://adventofcode.com/2021/day/24/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8').split('\n')[:-1]

    return data


def solve(data: List[str], part_1: bool=True):
    digits: Dict[int, Tuple[int, int]] = dict()
    stack: List[Tuple[int, int]] = list()
    dig = 0
    push = False
    sub = 0
    
    for i, line in enumerate(data):
        _, *operands = line.rstrip().split(' ')
        if i % 18 == 4:
            push = operands[1] == '1'
        if i % 18 == 5:
            sub = int(operands[1])
        if i % 18 == 15:
            if push:
                stack.append((dig, int(operands[1])))
            else:
                sibling, add = stack.pop()
                diff = add + sub
                if diff < 0:
                    digits[sibling] = (-diff + 1, 9)
                    digits[dig] = (1, 9 + diff)
                else:
                    digits[sibling] = (1, 9 - diff)
                    digits[dig] = (1 + diff, 9)
            dig += 1
    
    if part_1:
        print(''.join(str(digits[d][1]) for d in sorted(digits.keys())))
    else:
        print(''.join(str(digits[d][0]) for d in sorted(digits.keys())))

def solve_q1(data: List[str]):
    solve(data)

def solve_q2(data: List[str]):
    solve(data, False)


if __name__ == '__main__':
    data = get_data()    
    solve_q1(data)
    solve_q2(data)
