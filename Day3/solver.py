import os
import requests

AOC_SESSION = os.environ['AOC_SESSION']

def get_data():
    data = requests.get('https://adventofcode.com/2021/day/3/input',
        cookies={'session': AOC_SESSION}).content
    data = data.decode('utf-8')
    data = data.split('\n')
    # manipulation
    return data


def solve_q1(data):
    pass


def solve_q2(data):
    pass


if __name__ == '__main__':
    data = get_data()
    solve_q1(data)
    solve_q2(data)
