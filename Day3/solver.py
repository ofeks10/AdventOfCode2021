import os
from typing import List
import requests

AOC_SESSION = os.environ['AOC_SESSION']

def get_data() -> List[str]:
    data : List[str] = requests.get('https://adventofcode.com/2021/day/3/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8').split('\n')

    return data


def solve_q1(data: List[str]):
    gamma_rate = ''
    epsilon_rate = ''

    for i in range(len(data[0])):
        ones = 0
        zeros = 0
        for line in data[:-1]:
            if line[i] == '1':
                ones += 1
            else:
                zeros += 1

        if ones > zeros:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'

    print(int(gamma_rate, 2) * int(epsilon_rate, 2))
    


def solve_q2(data: List[str]):
    data2 = data[:-1]
    data = data[:-1]

    for i in range(len(data[0])):
        ones = 0
        zeros = 0
        for line in data:
            if line[i] == '1':
                ones += 1
            else:
                zeros += 1

        if ones >= zeros:
            data = [item for item in data if item[i] == '1']
        else:
            data = [item for item in data if item[i] == '0']

    for i in range(len(data2[0])):
        ones = 0
        zeros = 0
        for line in data2:
            if line[i] == '1':
                ones += 1
            else:
                zeros += 1

        if len(data2) == 1:
            break
        if zeros <= ones:
            data2 = [item for item in data2 if item[i] == '0']
        else:
            data2 = [item for item in data2 if item[i] == '1']

    print(len(data), len(data2))
 
    print(int(data[0], 2) * int(data2[0], 2))


if __name__ == '__main__':
    data = get_data()
    solve_q1(data)
    solve_q2(data)
