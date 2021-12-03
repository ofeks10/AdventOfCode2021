import os
from typing import List
import requests

AOC_SESSION = os.environ['AOC_SESSION']

def get_data() -> List[str]:
    data : List[str] = requests.get('https://adventofcode.com/2021/day/3/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8').split('\n')

    return data[:-1]


def solve_q1(data: List[str]):
    gamma_rate = ''
    epsilon_rate = ''

    for i in range(len(data[0])):
        ones = sum(1 for line in data if line[i] == '1')
        zeros = sum(1 for line in data if line[i] == '0')
        gamma_rate += '1' if ones > zeros else '0'
        epsilon_rate += '1' if ones < zeros else '0'

    print(int(gamma_rate, 2) * int(epsilon_rate, 2))
    


def solve_q2(data: List[str]):
    data2 = data.copy()

    for i in range(len(data[0])):
        ones = sum(1 for line in data if line[i] == '1')
        zeros = sum(1 for line in data if line[i] == '0')
        ones_data2 = sum(1 for line in data2 if line[i] == '1')
        zeros_data2 = sum(1 for line in data2 if line[i] == '0')

        # if they're equal the written one in the dict is the correct one
        hack = {zeros: '0', ones: '1'}
        data = [item for item in data if item[i] == hack[max(ones, zeros)]]

        if len(data2) > 1:
            # Because we're removing the ones with less values we need
            # to make sure we don't remove the last value
            hack = {ones_data2: '1', zeros_data2: '0'}
            data2 = [item for item in data2 if item[i] == hack[min(zeros_data2, ones_data2)]]

    print(int(data[0], 2) * int(data2[0], 2))


if __name__ == '__main__':
    data = get_data()
    solve_q1(data)
    solve_q2(data)
