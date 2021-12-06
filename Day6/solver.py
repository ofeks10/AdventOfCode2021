from collections import Counter
import os
from typing import Dict, List
import requests


AOC_SESSION = os.environ['AOC_SESSION']


def get_data() -> List[int]:
    data : List[str] = requests.get('https://adventofcode.com/2021/day/6/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8').split('\n')[:-1]

    fish: List[int] = list(map(int, data[0].split(',')))
    
    return fish

def counter(days: int, data: Dict[int, int]):
    for _ in range(days):
        new_fishes = data[0]
        for i in range(9):
            data[i] = data[(i+1)] if i != 8 else new_fishes
            if i == 6:
                data[i] += new_fishes

    print(sum(data.values()))


def solve_q1(data: List[int]) -> None:
    c = Counter(data)
    fishes_count = {i: c[i] for i in range(9)}

    counter(80, fishes_count)
    

def solve_q2(data: List[int]):
    c = Counter(data)
    fishes_count = {i: c[i] for i in range(9)}
    
    counter(256, fishes_count)


if __name__ == '__main__':
    data = get_data()    
    solve_q1(data)
    solve_q2(data)
