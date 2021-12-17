import os
from typing import Callable, List, Tuple
import requests


AOC_SESSION = os.environ['AOC_SESSION']


def get_data() -> Tuple[int, int, int, int]:
    data : List[str] = requests.get('https://adventofcode.com/2021/day/17/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8').split('\n')[:-1]

    d = data[0].split('..')
    start_x = int(d[0].split('=')[1])
    end_x = int(d[1].split(',')[0])
    start_y = int(d[1].split('=')[1])
    end_y = int(d[2].split(',')[0])

    return start_x, end_x, start_y, end_y


def solve_q1(start_x: int, end_x: int, start_y: int, end_y: int):
    min_y = min(start_y, end_y)
    max_y = max(start_y, end_y)
    calc_location = lambda v0, t: v0*t - (0.5 * t**2)
    locs_y = []
    for start_vel in range(250):
        for t in range(500):
            if min_y <= calc_location(start_vel, t) <= max_y:
                locs_y.append((start_vel, t))
    
    print(max(locs_y)[0] * (max(locs_y)[0] + 1) // 2)


def solve_q2(start_x: int, end_x: int, start_y: int, end_y: int):
    # start_x = 20
    # end_x = 30
    # start_y = -10
    # end_y = -5
    min_y = min(start_y, end_y)
    max_y = max(start_y, end_y)
    xs = []
    for cur_vel in range(1, end_x + 1):
        vel = cur_vel
        cur_x = 0
        for t in range(1, 500):
            if vel <= 0:
                vel = 0
            cur_x += vel
            vel -= 1
            if start_x <= cur_x <= end_x:
                xs.append((cur_vel, t))
    
    ys = []
    for start_vel in range(-250, 250):
        vel = start_vel
        cur_y = 0
        for t in range(1, 500):
            cur_y += vel
            vel -= 1
            if min_y <= cur_y <= max_y:
                ys.append((start_vel, t))

    print(xs)
    print(ys)
    print('\n\n')
    from collections import Counter
    c3 = Counter()
    total = set()
    # total = 0
    for c in ys:
        for c2 in xs:
            if c[1] == c2[1]:
                total.add((c2[0], c[0]))
    print(len(total), total)
    for c in total:
        if c[1] == -1:
            print(c)
        c3.update({c[1]: 1})
    print(c3)
    # import math
    # calc_location = lambda v0, t: v0*t - (0.5 * (t**2))
    # locs_y = []
    # locs_x = []
    # print('\n\n')
    # for start_vel in range(250, -500, -1):
    #     for t in range(1, end_x // 2):
    #         if start_x <= math.ceil(calc_location(start_vel, t)) <= end_x:
    #             locs_x.append((start_vel, t))
    #     for t in range(500):
    #         # maybe ciel
    #         if min_y <= math.ceil(calc_location(start_vel, t)) <= max_y:
    #             locs_y.append((start_vel, t))
    # print(locs_x)
    # print('\n\n\n')
    # total = 0
    # for loc in locs_y:
    #     for loc2 in locs_x:
    #         if loc2[1] == loc[1]:
    #             print(loc2[0], loc[0])
    #             total += 1
    # print(total)


if __name__ == '__main__':
    start_x, end_x, start_y, end_y = get_data()    
    solve_q1(start_x, end_x, start_y, end_y)
    solve_q2(start_x, end_x, start_y, end_y)
