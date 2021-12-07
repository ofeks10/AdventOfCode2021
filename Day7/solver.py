import os
from typing import List
import requests


AOC_SESSION = os.environ['AOC_SESSION']


def get_data() -> List[int]:
    data : List[str] = requests.get('https://adventofcode.com/2021/day/7/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8').split('\n')[:-1]

    crabs = list(map(int, data[0].split(',')))

    return crabs


def solve_q1(data: List[int]):
    data.sort()
    med = data[len(data) // 2]
    print(sum(abs(med - crab) for crab in data))

def solve_q2(data: List[int]):
    data.sort()
    s = lambda x: x * (x + 1) // 2
    print(min((sum(s(abs(crab - i)) for crab in data) for i in range(max(data)))))


if __name__ == '__main__':
    data = get_data()    
    solve_q1(data)
    solve_q2(data)
