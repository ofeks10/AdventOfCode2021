import os
from typing import DefaultDict, List, Set, Tuple
from collections import defaultdict
import requests


AOC_SESSION = os.environ['AOC_SESSION']


def get_data() -> List[List[int]]:
    data : List[str] = requests.get('https://adventofcode.com/2021/day/15/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8').split('\n')[:-1]

    # data = open('./Day15/example.in', 'r').read().split('\n')[:-1]

    maze = [[int(x) for x in row] for row in data]

    return maze


def get_adjacent(maze: List[List[int]], row: int, col: int) -> Set[Tuple[int, int]]:
    adjacent: Set[Tuple[int, int]] = set()
    if row > 0:
        adjacent.add((row - 1, col))
    if row < len(maze) - 1:
        adjacent.add((row + 1, col))
    if col > 0:
        adjacent.add((row, col - 1))
    if col < len(maze[0]) - 1:
        adjacent.add((row, col + 1))
    return adjacent


def find_shortest_path(maze: List[List[int]]):
    goal = (len(maze) - 1, len(maze[0]) - 1)
    visited: Set[Tuple[int, int]] = set()
    costs: DefaultDict[int, Set[Tuple[int, int]]] = defaultdict(set)
    costs[0].add((0, 0))

    for cost in range(100000000):
        for point in costs[cost]:
            if point == goal:
                return cost
            for adj in get_adjacent(maze, point[0], point[1]):
                if adj in visited:
                    continue
                visited.add(adj)
                costs[cost + maze[adj[0]][adj[1]]].add(adj)
    

def solve_q1(maze: List[List[int]]):
    print(find_shortest_path(maze))
    

def solve_q2(maze: List[List[int]]):
    new_maze = [[0] * 5 * len(maze[0]) for _ in range(5 * len(maze))]
    for i in range(5):
        for j in range(5):
            for k in range(len(maze)):
                for h in range(len(maze[0])):
                    new_maze[i * len(maze) + k][j * len(maze[0]) + h] =\
                        ((maze[k][h] + i + j - 1) % 9) + 1
    
    print(find_shortest_path(new_maze))


if __name__ == '__main__':
    maze = get_data()    
    solve_q1(maze)
    solve_q2(maze)
