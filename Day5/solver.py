from collections import Counter
import os
from typing import List
import requests


AOC_SESSION = os.environ['AOC_SESSION']


def get_data() -> List[List[int]]:
    data : List[str] = requests.get('https://adventofcode.com/2021/day/5/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8').split('\n')[:-1]
    
    points = [[int(i) for i in x.replace(' -> ', ',').split(',')] for x in data]
    
    return points


def my_range(start: int, end: int):
    if start < end:
        return range(start, end + 1)
    else:
        return range(start, end - 1, -1)


def solve_q1(data: List[List[int]]) -> Counter[int]:
    c: Counter[int] = Counter()

    for point in data:
        start_x = min(point[0], point[2])
        end_x = max(point[0], point[2])
        start_y = min(point[1], point[3])
        end_y = max(point[1], point[3])
 
        if start_x == end_x:
            c.update(map(lambda y: (start_x, y), my_range(start_y, end_y)))
        elif start_y == end_y:
            c.update(map(lambda x: (x, start_y), my_range(start_x, end_x)))

    print(sum([1 for item in c.values() if item >= 2]))
    return c


def solve_q2(data: List[List[int]], q1_counter: Counter[int]):
    for point in filter(lambda x: x[0] != x[2] and x[1] != x[3], data):
        q1_counter.update(zip(my_range(point[0], point[2]), my_range(point[1], point[3])))
    
    print(sum([1 for item in q1_counter.values() if item >= 2]))


if __name__ == '__main__':
    data = get_data()
    
    q1_counter = solve_q1(data)
    solve_q2(data, q1_counter)
