from collections import defaultdict
import os
from typing import DefaultDict, List, Tuple
import requests


AOC_SESSION = os.environ['AOC_SESSION']


def get_data() -> List[int]:
    data : List[str] = requests.get('https://adventofcode.com/2021/day/21/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8').split('\n')[:-1]

    players_pos = [int(line.split(': ')[1]) for line in data]

    return players_pos


def solve_q1(players_pos: List[int]):
    die = 1
    p1_score = 0
    p2_score = 0
    p1_pos = players_pos[0] - 1
    p2_pos = players_pos[1] - 1
    roll_count = 0
        
    while p1_score < 1000 and p2_score < 1000:
        for _ in range(3):
            p1_pos += die
            die += 1
            die = 1 if die % 101 == 0 else die
            roll_count += 1

        p1_pos %= 10
        p1_score += (p1_pos + 1)

        if p1_score >= 1000:
            break
        
        for _ in range(3):
            p2_pos += die
            die += 1
            die = 1 if die % 101 == 0 else die
            roll_count += 1
        p2_pos %= 10
        p2_score += (p2_pos + 1)

    print(min(p1_score, p2_score) * roll_count)


def solve_q2(data: List[int]):
    turn = 0
    universes: DefaultDict[Tuple[int, int, int, int], int] = defaultdict(int)
    universes[(data[0], data[1], 0, 0)] = 1

    possible_rolls: DefaultDict[int , int] = defaultdict(int)
    for d1 in range(1, 4):
        for d2 in range(1, 4):
            for d3 in range(1, 4):
                possible_rolls[d1+d2+d3] += 1

    in_progress = True
    while in_progress:
        in_progress = False
        next_universe: DefaultDict[Tuple[int, int, int, int], int] = defaultdict(int)
        for key in universes:
            p1, p2, s1, s2 = key
            if max([s1, s2]) < 21:
                in_progress = True
                for roll in possible_rolls:
                    p1, p2, s1, s2 = key
                    if turn == 0:
                        p1 = (p1 - 1 + roll) % 10 + 1
                        s1 += p1
                    else:
                        p2 = (p2 - 1 + roll) % 10 + 1
                        s2 += p2
                    next_universe[(p1, p2, s1, s2)] += possible_rolls[roll] * universes[key]
            else:
                if universes[key]:
                    next_universe[key] += universes[key]
                    
        universes = next_universe
        turn = (turn + 1) % 2

    win1 = sum([count for key, count in universes.items() if key[2] >= 21])
    win2 = sum([count for key, count in universes.items() if key[3] >= 21])

    print(max(win1, win2))


if __name__ == '__main__':
    players_pos = get_data()    
    solve_q1(players_pos)
    solve_q2(players_pos)
