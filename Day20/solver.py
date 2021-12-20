import os
from typing import DefaultDict, List, Tuple
import requests
from collections import defaultdict


AOC_SESSION = os.environ['AOC_SESSION']


def get_data() -> Tuple[List[int], DefaultDict[Tuple[int, int], int], Tuple[int ,int]]:
    data : str = requests.get('https://adventofcode.com/2021/day/20/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8')

    key_string, image_string = data.strip().split('\n\n')
    key = [1 if c == '#' else 0 for c in key_string]

    image: DefaultDict[Tuple[int, int], int] = defaultdict(int)
    for y, line in enumerate(image_string.split('\n')):
        for x, c in enumerate(line):
            if c == '#':
                image[x, y] = 1
        
    return key, image, (len(image_string.split('\n')[0]), len(image_string.split('\n')))


def enhance_image(
    key: List[int],
    image: DefaultDict[Tuple[int, int], int],
    low_coords: Tuple[int, int],
    high_coords: Tuple[int, int],
    steps: int) -> DefaultDict[Tuple[int, int], int]:

    infinite_bit = 0
    min_x, min_y = low_coords
    max_x, max_y = high_coords
    
    for _ in range(steps):
        next_image: DefaultDict[Tuple[int, int], int] = defaultdict(int)
        
        for x in range(min_x - 1, max_x + 2):
            for y in range(min_y - 1, max_y + 2):
                val = 0

                for cx, cy in (
                    (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                    (x - 1, y), (x, y), (x + 1, y),
                    (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)):
                    val <<= 1
                    val |= image[cx, cy] if min_x <= cx <= max_x and min_y <= cy <= max_y else infinite_bit
                
                if key[val] == 1:
                    next_image[x, y] = key[val]
        
        image = next_image
        infinite_bit = key[511 * infinite_bit]

        min_x -= 1
        min_y -= 1
        max_x += 1
        max_y += 1

    return image


def solve_q1(key: List[int], image: DefaultDict[Tuple[int, int], int], high_cords: Tuple[int, int]):
    enhanced = enhance_image(key, image, (0, 0), high_cords, 2)
    print(f'{sum(enhanced.values())}')

def solve_q2(key: List[int], image: DefaultDict[Tuple[int, int], int], high_cords: Tuple[int, int]):
    enhanced = enhance_image(key, image, (0, 0), high_cords, 50)
    print(f'{sum(enhanced.values())}')


if __name__ == '__main__':
    key, img, high_cords = get_data()    
    solve_q1(key, img, high_cords)
    solve_q2(key, img, high_cords)
