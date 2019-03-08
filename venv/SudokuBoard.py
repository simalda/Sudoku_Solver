from Backtraking import Backtraking
from Cell import Cell

import json

class SudokuBoard(object):
    def __init__(self, level, board_file='', solution =[],board = []):
        self.solution = solution
        self.board = board
        #if board_file!='':
           # self.__load_board(board_file)
        #else:
        self.board, self.solution = self.__create_board(level)


    def __create_board(self, level):
        b =  Backtraking()
        b.sudokuSolver(level)
        print('sudoku BOARD from BOARD')
        print(b.board)
        print('solution  ',b.solution)
        return b.board, b.solution

    def __load_board(self, board_file):
        f = open(board_file, "r+")
        for i in range(9):
            self.board.append(list(f.readline().strip('\n')))
        for i in range(11,19):
            self.solution.append(list(f.readline().strip('\n')))
        f.close()
        #return self.board, self.solution



