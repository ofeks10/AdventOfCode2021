import os
from typing import List, Optional, Set, Tuple
from dataclasses import dataclass
from functools import cache
import requests


AOC_SESSION = os.environ['AOC_SESSION']


def get_data() -> List[Tuple[int, List[int]]]:
    data : List[str] = requests.get('https://adventofcode.com/2021/day/22/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8').split('\n')[:-1]

    final_data: List[Tuple[int, List[int]]] = []
    on_off = [1 if 'on' in line.split(' ')[0] else 0 for line in data]
    
    for i, c in enumerate(data):
        actual_nums: List[int] = []
        numbers = [line.split(',')[0] for line in c.split('=')[1:]]
        for num in numbers:
            actual_nums.extend([int (x) for x in num.split('..')])
        final_data.append((on_off[i], actual_nums))
    
    return final_data


def solve_q1(data: List[Tuple[int, List[int]]]):
    on_bits: Set[Tuple[int, int, int]] = set()
    for line in data:
        for x in range(line[1][0], line[1][1] + 1):
            for y in range(line[1][2], line[1][3] + 1):
                for z in range(line[1][4], line[1][5] + 1):
                    if line[0] == 1:
                        on_bits.add((x, y, z))
                    else:
                        if (x, y, z) in on_bits:
                            on_bits.remove((x, y, z))
    
    print(len(on_bits))


@cache
def r_intersect(r1: range, r2: range) -> range:
    start_1, end_1, start_2, end_2 = r1[0], r1[-1], r2[0], r2[-1]
    if end_2 < start_1 or end_1 < start_2:
        return range(0)
    return range(min(end_2, max(start_1, start_2)), min(end_2, max(end_1, start_2)) + 1)


@dataclass
class Cube:
    state: bool
    x_range: range
    y_range: range
    z_range: range

    x_min = property(lambda self: self.x_range[0])
    y_min = property(lambda self: self.y_range[0])
    z_min = property(lambda self: self.z_range[0])
    x_max = property(lambda self: self.x_range[-1])
    y_max = property(lambda self: self.y_range[-1])
    z_max = property(lambda self: self.z_range[-1])

    def __init__(self, state: bool, *data: range):
        self.state, (self.x_range, self.y_range, self.z_range) = state, data

    @classmethod
    def from_cords(cls, state: bool, x_min: int, x_max: int, y_min: int, y_max: int, z_min: int, z_max: int) -> 'Cube':
        return cls(
            state,
            range(x_min, x_max + 1),
            range(y_min, y_max + 1),
            range(z_min, z_max + 1)
        )
        
    def __and__(self, other: 'Cube') -> 'Cube':
        return self.intersect(other, True)
    
    def intersect(self, other: 'Cube', state: Optional[bool] = None) -> 'Cube':
        return Cube(
            state if state is not None else self.state,
            r_intersect(self.x_range, other.x_range),
            r_intersect(self.y_range, other.y_range),
            r_intersect(self.z_range, other.z_range)
        )

    def volume(self) -> int:
        return len(self.x_range) * len(self.y_range) * len(self.z_range)


def specific_volume(cubes: List[Cube]) -> int:
    conflicts = [c for cube in cubes[1:] if (c := cubes[0] & cube).volume() > 0]
    return cubes[0].volume() - total_volume(conflicts)


def total_volume(cubes: List[Cube]) -> int:
    return sum(
        specific_volume(cubes[index:])
        for index, _ in enumerate(cubes)
        if cubes[index].state
    )


def solve_q2(data: List[Tuple[int, List[int]]]):
    cubes: List[Cube] = []
    for line in data:
        cubes.append(Cube.from_cords(bool(line[0]), *line[1]))
    
    print(total_volume(cubes))
    


if __name__ == '__main__':
    data = get_data()    
    solve_q1(data[:20])
    solve_q2(data)
