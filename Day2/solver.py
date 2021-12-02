import os
import requests

AOC_SESSION = os.environ['AOC_SESSION']

def get_data():
    data = requests.get(f'https://adventofcode.com/2021/day/2/input',
        cookies={'session': AOC_SESSION}).content
    data = data.decode('utf-8').split('\n')
    data = [item.split(' ') for item in data[:-1]] # ignore the last line for being empty
    data = [(item[0], int(item[1])) for item in data]

    return data


def solve_q1(data):
    horiz = 0
    depth = 0
    
    for action, amount in data:
        if action == 'forward':
            horiz += amount
        elif action == 'down':
            depth += amount
        elif action == 'up':
            depth -= amount
            
    print(horiz * depth)


def solve_q2(data):
    horiz = 0
    depth = 0
    aim = 0
    
    for action, amount in data:
        if action == 'forward':
            horiz += amount
            depth += (aim * amount)
        elif action == 'down':
            aim += amount
        elif action == 'up':
            aim -= amount
            
    print(horiz * depth)


if __name__ == '__main__':
    data = get_data()
    solve_q1(data)
    solve_q2(data)
