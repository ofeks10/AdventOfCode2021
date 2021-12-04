import os
from typing import List
import requests


AOC_SESSION = os.environ['AOC_SESSION']


class BingoBoard:
    def __init__(self, board) -> None:
        self.board = board
        self.board_with_marks = [[(x, False) for x in item] for item in self.board]

    def check_if_row(self):
        for row in self.board_with_marks:
            s = sum([x[1] for x in row])
            if s == 5:
                return True

        return False

    def check_if_column(self):
        for i in range(5):
            column_sum = 0
            for row in self.board_with_marks:
                if row[i][1]:
                    column_sum += 1
            if column_sum == 5:
                return True

        return False
    
    def calculate_falses(self):
        total = 0
        for row in self.board_with_marks:
            for item in row:
                if not item[1]:
                    total += item[0]
        return total
    
    def print(self):
        for row in self.board_with_marks:
            for item in row:
                print(item, end=' ')
            print()

    def mark(self, number):
        new_board = []
        for row in self.board_with_marks:
            current_row = []
            for item in row:
                if item[0] == number or item[1]:
                    current_row.append((item[0], True))
                else:
                    current_row.append((item[0], False))
            new_board.append(current_row)
        
        self.board_with_marks = new_board
        

def get_data() -> list[int]:
    data : str = requests.get('https://adventofcode.com/2021/day/4/input',
        cookies={'session': AOC_SESSION}).content.decode('utf-8')

    data_list = [x for x in data.split('\n')[:-1]]

    numbers_line = [int(x) for x in data_list[0].split(',')]
    boards_list = []
    for i in range(2, len(data_list), 6):
        current_board = []
        for j in range(5):
            current_board.append([int(x) for x in data_list[i + j].split()])
        boards_list.append(current_board)

    return numbers_line, [BingoBoard(x) for x in boards_list]


def solve_q1(numbers, boards):
    for number in numbers:
        for board in boards:
            board.mark(number)
            
            if board.check_if_row() or board.check_if_column():
                print(board.calculate_falses() * number)
                return
        

    
def solve_q2(numbers, boards):
    new_boards = boards.copy()
    for number in numbers:
        boards_that_won = []
        for board in new_boards:
            board.mark(number)

            if board.check_if_row() or board.check_if_column():
                boards_that_won.append(board)
        
        if len(new_boards) == 1 and (board.check_if_row() or board.check_if_column()):
            # new_boards[0].print()
            print(number * board.calculate_falses()) 

        for b in boards_that_won:
            new_boards.remove(b)



if __name__ == '__main__':
    numbers, boards = get_data()
    solve_q1(numbers, boards)
    solve_q2(numbers, boards)
