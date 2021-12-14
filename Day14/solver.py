import os
from collections import Counter
from typing import Tuple, Dict, Counter, List
import requests


AOC_SESSION = os.environ['AOC_SESSION']


def get_data() -> Tuple[str, Dict[str, str]]:
    data : List[str] = requests.get('https://adventofcode.com/2021/day/14/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8').split('\n')[:-1]
    
    starting = data[0]
    insersions = {line.split(' -> ')[0]: line.split(' -> ')[1] for line in data[2:]}

    return starting, insersions


def solve_q1(starting: str, insersions: Dict[str, str]):
    new_string = starting
    for _ in range(10):
        current = new_string[0]
        for i in range(len(new_string) - 1):
            current += insersions[new_string[i:i+2]] + new_string[i+1]
        new_string = current
    
    # print(len(new_string))
    
    c = Counter(new_string)
    print(int(c.most_common(1)[0][1]) - int(c.most_common()[-1][1]))


def solve_q2(starting: str, insersions: Dict[str, str]):
    pairs_counter: Counter[str] = Counter()
    single_char_counter = Counter(starting)

    for k, v in zip(starting, starting[1:]):
        pairs_counter[k + v]+=1

    better_insersions = {k: [k[0] + v, v + k[1]] for k, v in insersions.items()}
    
    for _ in range(40):
        current_counter: Counter[str] = Counter()
        for pair, count in pairs_counter.items():
            if pair in better_insersions:
                single_char_counter[better_insersions[pair][0][1]] += count
                for new_pair in better_insersions[pair]:
                    current_counter[new_pair] += count
        pairs_counter = current_counter
    
    print(single_char_counter.most_common(1)[0][1] - single_char_counter.most_common()[-1][1])


if __name__ == '__main__':
    starting, insersions = get_data()    
    solve_q1(starting, insersions)
    # print(starting)
    solve_q2(starting, insersions)
