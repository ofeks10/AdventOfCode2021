import os
from collections import Counter
from typing import Tuple, Dict, Counter, List
import requests


AOC_SESSION = os.environ['AOC_SESSION']


def get_data() -> Tuple[str, Dict[str, List[str]]]:
    data : List[str] = requests.get('https://adventofcode.com/2021/day/14/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8').split('\n')[:-1]
    
    starting = data[0]
    insersions = {line.split(' -> ')[0]: line.split(' -> ')[1] for line in data[2:]}
    better_insersions = {k: [k[0] + v, v + k[1]] for k, v in insersions.items()}

    return starting, better_insersions


def solve(starting: str, insersions: Dict[str, List[str]], amount: int):
    pairs_counter: Counter[str] = Counter()
    single_char_counter = Counter(starting)

    for k, v in zip(starting, starting[1:]):
        pairs_counter[k + v]+=1

    for _ in range(amount):
        current_counter: Counter[str] = Counter()
        for pair, count in pairs_counter.items():
            if pair in insersions:
                single_char_counter[insersions[pair][0][1]] += count
                for new_pair in insersions[pair]:
                    current_counter[new_pair] += count
        pairs_counter = current_counter
    
    return single_char_counter.most_common(1)[0][1] - single_char_counter.most_common()[-1][1]


def solve_q1(starting: str, insersions: Dict[str, List[str]]):
    print(solve(starting, insersions, 10))


def solve_q2(starting: str, insersions: Dict[str, List[str]]):
    print(solve(starting, insersions, 40))


if __name__ == '__main__':
    starting, insersions = get_data()    
    solve_q1(starting, insersions)
    # print(starting)
    solve_q2(starting, insersions)
