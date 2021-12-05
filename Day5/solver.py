import os
from typing import List, Tuple
import requests


AOC_SESSION = os.environ['AOC_SESSION']


class Point:
    def __init__(self, from_point: str, to_point: str) -> None:
        self.from_x, self.from_y = map(int, from_point.split(','))
        self.to_x, self.to_y = map(int, to_point.split(','))

    def is_vertical(self):
        return int(self.from_x) == int(self.to_x)

    def is_horizontal(self):
        return int(self.from_y) == int(self.to_y)

    def is_diagonal(self):
        return not self.is_horizontal() and not self.is_vertical()


def get_data() -> List[Point]:
    data : List[str] = requests.get('https://adventofcode.com/2021/day/5/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8').split('\n')[:-1]
    # data = open('./Day5/test.in').readlines()
    # data = open('/home/ofeks10/Downloads/input.txt').readlines()
    points: List[Point] = []
    for line in data:
        from_point, to_point = line.split(' -> ')
        points.append(Point(from_point, to_point))
    
    return points


def solve_q1(points: List[Point]):
    max_x = max(int(point.to_x) for point in points)
    max_y = max(int(point.to_y) for point in points)

    board = [[0 for i in range(max_x + 5)] for j in range(max_y + 5)]

    for point in points:
        if point.is_horizontal():
            for i in range(min(int(point.from_x), int(point.to_x)), max(int(point.from_x), int(point.to_x)) + 1):
                board[int(point.from_y)][i] += 1
        elif point.is_vertical():
            for i in range(min(int(point.from_y), int(point.to_y)), max(int(point.from_y), int(point.to_y)) + 1):
                board[i][int(point.from_x)] += 1
   
    print(sum(sum(1 for i in row if i >= 2) for row in board))
    return board
        

def my_range(start, end):
    if start > end:
        return range(start, end -1, -1)
    else:
        return range(start, end + 1)

def solve_q2(points: List[Point], board: List[List[int]]):
    new_board = board.copy()

    for point in filter(lambda x: x.is_diagonal(), points):
        start_x = point.from_x
        end_x = point.to_x
        start_y = point.from_y
        end_y = point.to_y

        # print(point.from_x, point.from_y, point.to_x, point.to_y)
        # print(start_x, start_y, end_x, end_y)

        for x, y in zip(my_range(start_x, end_x), my_range(start_y, end_y)):
            new_board[y][x] += 1

    print(sum(sum(1 for i in row if i >= 2) for row in new_board))

if __name__ == '__main__':
    data = get_data()
    
    board = solve_q1(data)
    solve_q2(data, board)
