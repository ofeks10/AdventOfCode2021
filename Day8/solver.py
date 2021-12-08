import os
from typing import Callable, Dict, List, Tuple
from collections import Counter
from itertools import permutations
import requests


AOC_SESSION = os.environ['AOC_SESSION']


def get_data() -> Tuple[List[List[str]], List[List[str]]]:
    data : List[str] = requests.get('https://adventofcode.com/2021/day/8/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8').split('\n')[:-1]

    # data = open('./Day8/example.in', 'r').read().split('\n')[:-1]

    signals = []
    output = []
    for line in data:
        signals.append(line.split(' | ')[0].split(' '))
        output.append(line.split(' | ')[1].split(' '))

    return signals, output


def solve_q1(output: List[List[str]]):
    output_flat = [item for sublist in output for item in sublist]
    c = Counter([len(out) for out in output_flat])
    print (c[2] + c[3] + c[4] + c[7])

def solve_q2(signals: List[List[str]], output: List[List[str]]):
    numbers = {
        "abcefg": "0",
        "cf": "1",
        "acdeg": "2",
        "acdfg": "3",
        "bcdf": "4",
        "abdfg": "5",
        "abdefg": "6",
        "acf": "7",
        "abcdefg": "8",
        "abcdfg": "9",
    }

    total_sum = 0

    for signal, out in zip(signals, output):
        for perm in permutations('abcdefg'):
            mapping = dict(zip(perm, 'abcdefg'))
            reverse_mapping = {v: k for k, v in mapping.items()}
            join_sorted: Callable[[str, Dict[str, str]], str] = lambda x, y: ''.join(sorted(y[i] for i in x))
            decoded_set = set(
                join_sorted(number, mapping) for number in numbers.keys()
            )
            signal_set = set(''.join(sorted(sig)) for sig in signal)
            if decoded_set == signal_set:
                total_sum += int(''.join(numbers[join_sorted(digit, reverse_mapping)] for digit in out))
    
    print(total_sum)


if __name__ == '__main__':
    signals, output = get_data()    
    solve_q1(output)
    solve_q2(signals, output)
