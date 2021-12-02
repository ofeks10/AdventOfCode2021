import os
import requests


AOC_SESSION = os.environ['AOC_SESSION']

def get_data():
    data = requests.get('https://adventofcode.com/2021/day/1/input', cookies={'session': AOC_SESSION}).content
    data = data.decode('utf-8')
    data = data.split('\n')
    data = [int(x) for x in data[:-1]]
    return data


def solve_q1(data):
    total = 0
    
    for i in range(len(data) - 1):
        if data[i] < data[i + 1]:
            total += 1
    
    print(total)

    
def solve_q2(data):
    total = 0
    
    for i in range(len(data) - 3):
        first_sum = data[i] + data[i + 1] + data[i + 2]
        second_sum = data[i +  1] + data[i + 2] + data[i + 3]
        if first_sum < second_sum:
            total += 1
            
    print(total)
    
if __name__ == '__main__':
    data = get_data()
    solve_q1(data)
    solve_q2(data)
