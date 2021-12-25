import os
from typing import List
import requests


AOC_SESSION = os.environ['AOC_SESSION']


def get_data() -> List[str]:
    data : List[str] = requests.get('https://adventofcode.com/2021/day/25/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8').split('\n')[:-1]

    return data


def move(field: List[str], cucumber: str) -> List[str]:
    new_field = [['.'] for _ in range(len(field))]

    for i in range(len(field)):
        if field[i][0] == '.' and field[i][-1] == cucumber:
            new_field[i] = list(field[i])
            new_field[i][0], new_field[i][-1] = cucumber, '.'
            field[i] = ''.join(new_field[i])
            field[i] = field[i][0] \
                + field[i][1:-1].replace(cucumber + '.', '.' + cucumber) \
                + field[i][-1]
            continue
        field[i] = field[i].replace(cucumber + '.', '.' + cucumber)
    
    return [''.join(row[col] for row in field) for col in range(len(field[0]))]
        


def solve_q1(data: List[str]):
    field = move(move(data, '>'), 'v')
    rounds = 1
    stack = ''

    while stack != "".join(field):
        # if no string conversion, old stack overwritten at one point?!?!
        stack = "".join(field)
        field = move(move(field, ">"), "v")
        rounds += 1
    
    print(rounds)


if __name__ == '__main__':
    data = get_data()    
    solve_q1(data)
