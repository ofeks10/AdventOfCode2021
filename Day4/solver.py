import os
from typing import List, Tuple
import requests


AOC_SESSION = os.environ['AOC_SESSION']
BOARD_HEIGHT = 5
BOARD_WIDTH = 5
STARTING_BOARD_ROW = 2
SPACE_LINES_BETWEEN_ROWS = 1


class BingoBoard:
    def __init__(self, board: List[List[int]]) -> None:
        self.board_with_marks: List[List[List[int]]] = [[[x, False] for x in item] for item in board]
        self.won = False

    def check_if_row(self):
        if self.won:
            return self.won
        
        condition = 5 in [sum([x[1] for x in row]) for row in self.board_with_marks]
        self.won = condition
        return condition

    def check_if_column(self):
        if self.won:
            return self.won
        
        columns = [[row[j] for row in self.board_with_marks] for j in range(len(self.board_with_marks))]
        condition = 5 in [sum([x[1] for x in row]) for row in columns]
        self.won = condition
        return condition
    
    def calculate_falses(self):
        items = [[x[0] for x in row if not x[1]] for row in self.board_with_marks]
        return sum([sum([item for item in row]) for row in items])
    
    def print(self):
        for row in self.board_with_marks:
            for item in row:
                print(item, end=' ')
            print()

    def mark(self, number: int):
        self.board_with_marks = [[[item[0], True] if item[0] == number else item for item in row] for row in self.board_with_marks]        


def get_data() -> Tuple[List[int], List[BingoBoard]]:
    data : str = requests.get('https://adventofcode.com/2021/day/4/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8')

    data_list = [x for x in data.split('\n')[:-1]]

    numbers_line = [int(x) for x in data_list[0].split(',')]
    boards_list: List[List[List[int]]] = []

    for i in range(STARTING_BOARD_ROW, len(data_list), BOARD_HEIGHT + SPACE_LINES_BETWEEN_ROWS):
        current_board: List[List[int]] = []

        for j in range(BOARD_WIDTH):
            current_board.append([int(x) for x in data_list[i + j].split()])

        boards_list.append(current_board)

    return numbers_line, [BingoBoard(x) for x in boards_list]


def solve_q1(numbers: List[int], boards: List[BingoBoard]):
    for number in numbers:
        for board in boards:
            board.mark(number)
            
            if board.check_if_row() or board.check_if_column():
                print(board.calculate_falses() * number)
                return
        

    
def solve_q2(numbers: List[int], boards: List[BingoBoard]):
    current_boards = boards.copy()
    for number in numbers:
        current_boards = [board for board in current_boards if not board.won]
        for board in current_boards:
            board.mark(number)
        
            if (board.check_if_row() or board.check_if_column()) and len(current_boards) == 1:
                print(number * board.calculate_falses())
                return


if __name__ == '__main__':
    numbers, boards = get_data()
    solve_q1(numbers, boards)
    solve_q2(numbers, boards)
