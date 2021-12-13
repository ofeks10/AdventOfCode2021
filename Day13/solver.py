import os
from typing import List, Set, Tuple
from copy import deepcopy
import requests


AOC_SESSION = os.environ['AOC_SESSION']


def get_data() -> Tuple[Set[Tuple[int, int]], List[Tuple[str, int]]]:
    data : List[str] = requests.get('https://adventofcode.com/2021/day/13/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8').split('\n')[:-1]
    
    points = set([(int(x.split(',')[0]), int(x.split(',')[1])) for x in data if ',' in x])
    folds = [(x.split('=')[0][-1], int(x.split('=')[1])) for x in data if '=' in x]

    return points, folds


def perform_fold(points: Set[Tuple[int, int]], fold: Tuple[str, int]):
    new_points: Set[Tuple[int, int]] = set()

    if fold[0] == 'x':
        for point in points:
            if point[0] < fold[1]:
                new_points.add(point)
            elif point[0] > fold[1] and 2*fold[1] - point[0] >= 0:
                new_points.add((2*fold[1] - point[0], point[1]))
    else:
        for point in points:
            if point[1] < fold[1]:
                new_points.add(point)
            elif point[1] > fold[1] and 2*fold[1] - point[1] >= 0:
                new_points.add((point[0], 2*fold[1] - point[1]))
    
    return new_points


def solve_q1(points: Set[Tuple[int, int]], folds: List[Tuple[str, int]]):
    print('starting')
    new_points = deepcopy(points)
    print(len(perform_fold(new_points, folds[0])))

def solve_q2(points: Set[Tuple[int, int]], folds: List[Tuple[str, int]]):
    new_points = deepcopy(points)

    # Perform all folds
    for fold in folds:
        new_points = perform_fold(new_points, fold)
    
    # Print the board
    max_y, max_x = (max(new_points, key=lambda x: x[1])[1], max(new_points, key=lambda x: x[0])[0])
    for i in range(max_y + 3):
        for j in range(max_x + 4):
            if (j, i) in new_points:
                print('#', end=' ')
            else:
                print('.', end=' ')
        print()




if __name__ == '__main__':
    points, folds = get_data()    
    solve_q1(points, folds)
    solve_q2(points, folds)
