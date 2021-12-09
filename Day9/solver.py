import os
from typing import Callable, List, Set, Tuple
from colorama import Fore, Style
import requests


AOC_SESSION = os.environ['AOC_SESSION']


def get_data() -> List[List[int]]:
    data : List[str] = requests.get('https://adventofcode.com/2021/day/9/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8').split('\n')[:-1]

    # data = open('Day9/example.in', 'r').read().split('\n')[:-1]
    # print(data)

    board = [[10 for _ in range(len(data[0]) + 2)] for _ in range(len(data) + 2)]
    for i in range(len(data)):
        for j in range(len(data[0])):
            # print(i, j)
            board[i + 1][j + 1] = int(data[i][j])

    return board

def is_low_point(data: List[List[int]], i: int, j: int):
    return data[i][j] < data[i + 1][j] and \
        data[i][j] < data[i - 1][j] and \
        data[i][j] < data[i][j + 1] and \
        data[i][j] < data[i][j - 1]


def solve_q1(data: List[List[int]]):
    s = sum(data[i][j] + 1 for i in range(1, len(data) - 1) for j in range(1, len(data[0]) - 1) if is_low_point(data, i, j))
    print(s)


def calc_basin_size(data: List[List[int]], next_num: int, i: int, j: int, calculated: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
    if (i, j) in calculated:
        return set()
    
    calculated.add((i, j))

    # print(i, j)
    if i != 0 and data[i - 1][j] != 9: # up
        calculated.update(calc_basin_size(data, next_num + 1, i - 1, j, calculated))
    
    if i != len(data) - 1 and data[i + 1][j] != 9: # down
        calculated.update(calc_basin_size(data, next_num + 1, i + 1, j, calculated))

    if j != 0 and data[i][j - 1] != 9: # left
        calculated.update(calc_basin_size(data, next_num + 1, i, j - 1, calculated))
    
    if j != len(data[0]) - 1 and data[i][j + 1] != 9: # right
        calculated.update(calc_basin_size(data, next_num + 1, i, j + 1, calculated))

    return calculated


def solve_q2(data: List[List[int]]):
    basin_sizes: List[int] = []
    total_low_points = 0
    for i in range(1, len(data) - 1):
        for j in range(1, len(data[0]) - 1):
            if is_low_point(data, i, j):
                total_low_points += 1
                test = calc_basin_size(data, data[i][j], i, j, set())
                length = len(test)
                basin_sizes.append(length)
                if length > 110:
                    print(i, j, data[i][j], test)
    
    basin_sizes.sort()
    print(total_low_points)
    print(len(basin_sizes))
    basin_sizes = [s for s in basin_sizes if s < 110]
    print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])


if __name__ == '__main__':
    data = get_data()    
    solve_q1(data)
    solve_q2(data)
