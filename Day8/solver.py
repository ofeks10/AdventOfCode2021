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
        'abcefg': '0',
        'cf': '1',
        'acdeg': '2',
        'acdfg': '3',
        'bcdf': '4',
        'abdfg': '5',
        'abdefg': '6',
        'acf': '7',
        'abcdefg': '8',
        'abcdfg': '9',
    }

    total_sum = 0

    for signal, out in zip(signals, output):
        for perm in permutations('abcdefg'):
            mapping = dict(zip(perm, 'abcdefg'))
            reverse_mapping = {v: k for k, v in mapping.items()}
            join_sorted: Callable[[str, Dict[str, str]], str] = lambda x, y: ''.join(sorted(y[i] for i in x))
            decoded = sorted([join_sorted(number, mapping) for number in numbers.keys()])
            signal_sorted = sorted([''.join(sorted(sig)) for sig in signal])
            
            if decoded == signal_sorted:
                total_sum += int(''.join(numbers[join_sorted(digit, reverse_mapping)] for digit in out))
    
    print(total_sum)


def solve_q2_better(signals: List[List[str]], output: List[List[str]]):
    numbers = {
        'abcefg': '0',
        'cf': '1',
        'acdeg': '2',
        'acdfg': '3',
        'bcdf': '4',
        'abdfg': '5',
        'abdefg': '6',
        'acf': '7',
        'abcdefg': '8',
        'abcdfg': '9',
    }

    total_sum = 0

    for signal_row, output_row in zip(signals, output):
        answer: Dict[str, str] = {}

        # Use the 1 to find the c and f, but without order
        cf = ''
        for signal in signal_row:
            if len(signal) == 2:
                cf = signal

        # find 6 because it can tell us the order of the cf of 1
        # because the 6 is lighting up the c or the f
        for signal in signal_row:
            if len(signal) == 6 and (cf[0] in signal)!=(cf[1] in signal):
                if cf[0] in signal:
                    answer[cf[0]] = 'f'
                    answer[cf[1]] = 'c'
                else:
                    answer[cf[0]] = 'c'
                    answer[cf[1]] = 'f'

        # now that we know the order of cf we can find using 7 the a.
        for signal in signal_row:
            if len(signal) == 3:
                for letter in signal:
                    if letter not in cf:
                        answer[letter] = 'a'

        # now that we know the 7 we can find using the 4 the b and d but without ordering
        bd = ''.join(filter(lambda x: x not in cf, ''.join(filter(lambda sig: len(sig) == 4, signal_row))))
        
        # we can now use the 0 to find whether the top is b or d
        for signal in signal_row:
            if len(signal) == 6 and (bd[0] in signal)!=(bd[1] in signal):
                if bd[0] in signal:
                    answer[bd[0]] = 'b'
                    answer[bd[1]] = 'd'
                else:
                    answer[bd[0]] = 'd'
                    answer[bd[1]] = 'b'

        # now that we know the b and d we can find the e and g using the 9
        eg = ''.join(filter(lambda x: x not in answer, ['a', 'b', 'c', 'd', 'e', 'f', 'g']))
        for signal in signal_row:
            if len(signal) == 6 and (eg[0] in signal)!=(eg[1] in signal):
                if eg[0] in signal:
                    answer[eg[0]] = 'g'
                    answer[eg[1]] = 'e'
                else:
                    answer[eg[0]] = 'e'
                    answer[eg[1]] = 'g'
        
        current_output_sum = ''
        for out in output_row:
            current_perm: str = ''
            for letter in out:
                current_perm += answer[letter]
            
            converted_number = [k for v, k in numbers.items() if v == ''.join(sorted(current_perm))][0]
            current_output_sum += converted_number

        total_sum += int(current_output_sum)

    print(total_sum)


if __name__ == '__main__':
    signals, output = get_data()    
    solve_q1(output)
    solve_q2_better(signals, output)
    # solve_q2(signals, output)
