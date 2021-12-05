from collections import Counter
import os
from typing import List
import requests


AOC_SESSION = os.environ['AOC_SESSION']


def get_data() -> List[int]:
    data : List[str] = requests.get('https://adventofcode.com/2021/day/6/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8').split('\n')[:-1]
    
    return []


def my_range(start: int, end: int):
    if start < end:
        return range(start, end + 1)
    else:
        return range(start, end - 1, -1)


def solve_q1(data: List[int]) -> None:
    print('yay')
    

def solve_q2(data: List[int]):
    print('yay2')


if __name__ == '__main__':
    data = get_data()    
    solve_q1(data)
    solve_q2(data)
