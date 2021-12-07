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
    min_crab = min(data)
    max_crab = max(data)
    min_fuel = 1000000000
    print(min_crab, max_crab)

    for i in range(min_crab, max_crab + 1):
        current_fuel = 0
        for crab in data:
            current_fuel += (abs(crab - i))

        if current_fuel < min_fuel:
            min_fuel = current_fuel
    
    print(min_fuel)

def solve_q2(data: List[int]):
    min_crab = min(data)
    max_crab = max(data)
    min_fuel = 1000000000
    print(min_crab, max_crab)

    for i in range(min_crab, max_crab + 1):
        # print(i)
        current_fuel = 0
        for crab in data:
            current_fuel += (sum(range(1, abs(crab - i) + 1)))

        if current_fuel < min_fuel:
            min_fuel = current_fuel
    
    print(min_fuel)


if __name__ == '__main__':
    data = get_data()    
    solve_q1(data)
    solve_q2(data)
