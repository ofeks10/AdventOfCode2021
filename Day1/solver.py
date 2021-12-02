import os
from typing import List
import requests


AOC_SESSION = os.environ['AOC_SESSION']

def get_data() -> list[int]:
    data : str = requests.get('https://adventofcode.com/2021/day/1/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8')

    data_list : List[int] = [int(x) for x in data.split('\n')[:-1]]

    return data_list


def solve_q1(data : List[int]):
    total = 0
    
    for i in range(len(data) - 1):
        if data[i] < data[i + 1]:
            total += 1
    
    print(total)

    
def solve_q2(data : List[int]):
    total = 0
    
    for i in range(len(data) - 3):
        first_sum : int = data[i] + data[i + 1] + data[i + 2]
        second_sum :int = data[i +  1] + data[i + 2] + data[i + 3]
        if first_sum < second_sum:
            total += 1
            
    print(total)
    
if __name__ == '__main__':
    data: List[int] = get_data()
    solve_q1(data)
    solve_q2(data)
