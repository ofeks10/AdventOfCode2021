import os
from typing import Dict, List, Set
from collections import defaultdict
import requests


AOC_SESSION = os.environ['AOC_SESSION']


def get_data() -> Dict[str, List[str]]:
    data : List[str] = requests.get('https://adventofcode.com/2021/day/12/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8').split('\n')[:-1]
    
    # data = open('./Day12/example.in', 'r').read().split('\n')[:-1]

    graph = defaultdict(list)
    for line in data:
        a, b = line.split('-')
        graph[a].append(b)
        graph[b].append(a)
    
    return graph


def count_graph_q1(graph: Dict[str, List[str]], current: str, end: str, visited: Set[str]) -> int:
    if current == end:
        return 1

    total = 0
    for node in graph[current]:
        if node in visited:
            continue
        new_visited = visited | {current} if current.islower() else visited
        total += count_graph_q1(graph, node, end, new_visited)

    return total

def solve_q1(data: Dict[str, List[str]]):
    print(count_graph_q1(data, 'start', 'end', set()))


def count_graph_q2(graph: Dict[str, List[str]], current: str, end: str, visited: Set[str], twice: str, path: List[str], paths: Set[str]) -> int:
    total = 0
    for node in graph[current]:
        if node in visited:
            continue

        if current == end:
            current_path = ''.join(path)
            if current_path not in paths:
                total += 1
                paths.add(current_path)
            continue

        if node.islower():
            if twice == '':
               total += count_graph_q2(graph, node, end, visited, node, path + [node], paths)
               total += count_graph_q2(graph, node, end, visited | {node}, '', path + [node], paths)
            else:
                total += count_graph_q2(graph, node, end, visited | {node}, twice, path + [node], paths)
        else:
            total += count_graph_q2(graph, node, end, visited, twice, path + [node], paths)
        
    return total


def solve_q2(data: List[int]):
    print(count_graph_q2(data, 'start', 'end', set(['start']), '', ['start'], set()))


if __name__ == '__main__':
    data = get_data()    
    solve_q1(data)
    solve_q2(data)
