import os
from typing import List, Set, Tuple
import requests


AOC_SESSION = os.environ['AOC_SESSION']


def get_data() -> List[List[int]]:
    data : List[str] = requests.get('https://adventofcode.com/2021/day/9/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8').split('\n')[:-1]

    board = [[10 for _ in range(len(data[0]) + 2)] for _ in range(len(data) + 2)]
    for i in range(len(data)):
        for j in range(len(data[0])):
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


def get_basin(data: List[List[int]], i: int, j: int, seen: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
    if (i, j) in seen:
        return set()
    
    seen.add((i, j))

    if data[i - 1][j] < 9 and i >= 1:
        get_basin(data, i - 1, j, seen)
    
    if data[i + 1][j] < 9 and i <= len(data) - 2:
        get_basin(data, i + 1, j, seen)

    if data[i][j - 1] < 9 and j >= 1:
        get_basin(data, i, j - 1, seen)
    
    if data[i][j + 1] < 9 and j <= len(data[i]) - 2:
        get_basin(data, i, j + 1, seen)
    
    return seen


def solve_q2(data: List[List[int]]):
    basin_sizes: List[int] = []
    for i in range(1, len(data) - 2):
        for j in range(1, len(data[i]) - 2):
            if is_low_point(data, i, j):
                basin_sizes.append(len(get_basin(data, i, j, set())))

    basin_sizes.sort()
    print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])


if __name__ == '__main__':
    data = get_data()    
    solve_q1(data)
    solve_q2(data)
