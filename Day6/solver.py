from collections import Counter
import os
from typing import Dict, List
import requests


AOC_SESSION = os.environ['AOC_SESSION']


def get_data() -> List[int]:
    data : List[str] = requests.get('https://adventofcode.com/2021/day/6/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8').split('\n')[:-1]

    # data = ['3,4,3,1,2']
    fish: List[int] = list(map(int, data[0].split(',')))
    
    return fish


def my_range(start: int, end: int):
    if start < end:
        return range(start, end + 1)
    else:
        return range(start, end - 1, -1)


def recurse_q1(days: int, data: List[int]):
    if days == 0:
        print(len(data))
        return

    for i in range(len(data)):
        if data[i] == 0:
            data[i] = 6
            data.append(8)
        else:
            data[i] -= 1

    recurse_q1(days - 1, data)

def solve_q1(data: List[int]) -> None:
    recurse_q1(80, data.copy())
    

def recurse_q2(days: int, data: Dict[int, int]):
    if days == 0:
        print(sum(data.values()))
        return
    
    temp = data[1]
    data[1] = data[2]
    data[2] = data[3]
    data[3] = data[4]
    data[4] = data[5]
    data[5] = data[6]
    data[6] = data[7]
    data[6] += data[0]
    data[7] = data[8]
    data[8] = data[0]
    data[0] = temp

    recurse_q2(days - 1, data)
    

def solve_q2(data: List[int]):
    fishes_count = {i: 0 for i in range(9)}
    for fish in data:
        fishes_count[fish] += 1
    recurse_q2(256, fishes_count)


if __name__ == '__main__':
    data = get_data()    
    solve_q1(data)
    solve_q2(data)
