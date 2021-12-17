import os
from typing import Callable, List, Set, Tuple
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

    # since the y's are negative, flip them
    return start_x, end_x, end_y, start_y


def solve_q1(start_x: int, end_x: int, start_y: int, end_y: int):
    # We can ignore the x because we understand the x can and will
    # at somepoint will reach the target area, but the important thing
    # here is the maximum y reached
    # The formula is that because the "gravity" is -1, we can see
    # that for a velocity V we will get back to 0 with a velocity of -V
    # so we just need to find the velocity for which we will reach the "maximum"
    # height in the negatives.  so using the n*(n+1) / 2 formula for a negative
    # velocity we can calculate the maximum height.
    print(-1 * end_y * ((-1 * end_y - 1) // 2))


def solve_q2(start_x: int, end_x: int, start_y: int, end_y: int):
    min_y = min(start_y, end_y)
    max_y = max(start_y, end_y)
    xs: List[Tuple[int, int]] = []
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
    
    ys: List[Tuple[int, int]] = []
    for start_vel in range(-250, 250):
        vel = start_vel
        cur_y = 0
        for t in range(1, 500):
            cur_y += vel
            vel -= 1
            if min_y <= cur_y <= max_y:
                ys.append((start_vel, t))

    total: Set[Tuple[int, int]] = set((c2[0], c[0]) for c2 in xs for c in ys if c[1] == c2[1])

    print(len(total))


if __name__ == '__main__':
    start_x, end_x, start_y, end_y = get_data()    
    solve_q1(start_x, end_x, start_y, end_y)
    solve_q2(start_x, end_x, start_y, end_y)
