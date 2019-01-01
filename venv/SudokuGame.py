from  SudokuBoard import SudokuBoard
import math
from tkinter.filedialog import *

class SudokuGame(object):
    def __init__(self, level, board_file=''):
        self.board_file = board_file
        start_puzzleForGame = []
        if board_file!='':
            self.start_puzzle = SudokuBoard('',board_file)
        else:
            self.start_puzzle =  SudokuBoard(level)

        self.RealPuzzle = []
        self.start_puzzleForGame = start_puzzleForGame
    def start(self):
        is_game_over = False
        self.RealPuzzle = self.duplicate()
        self.start_puzzleForGame = self.duplicate()

    def duplicate(self):
        puzzle = []
        for i in range(9):
            x = []
            for j in range(9):
                if self.start_puzzle.board[i][j]==0 or self.start_puzzle.board[i][j]=='0':
                   self.start_puzzle.board[i][j]=0
                x.append([self.start_puzzle.board[i][j],"black"])
            puzzle.append(x)
            print(puzzle)
        return puzzle
    def check_win(self, puzzle):
        for i in range(9):
             print("ffff",self.check_row(i,puzzle))
             if not self.check_row(i,puzzle):
                 return False
        for j in range(9):
             if not  self.check_column(j,puzzle):
                 return False
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                if not self.check_square(x,y,puzzle):
                    return False
        return True


    def check_row(self,row, puzzle):
        for i in range(9):
            row1 = list(map(lambda x: int(x[0]), puzzle[row]))
            if i+1 not in  row1:
                return False
        return True
    
    def check_column(self,column, puzzle):
        for i in range(9):
            column1 = list(map(lambda x: int(x[0]), puzzle[column]))
            if i+1 not in column1:
                return False
        return True
    
    def check_square(self, row, column, puzzle):
        square = []
        for i in range(3):
            for j in range(3):
                square.append(int(puzzle[row+i][column+j][0]))
        for i in range(9):
            if i+1 not in square:
               return False
        return True

    def check_board(self):
        for i in range(9):
            for j in range(9):
                if self.RealPuzzle[i][j][1] == "red":
                    self.RealPuzzle[i][j][1] = "green"
                    k =  i+1
                    l = j+1
                    self.check_move(k, l, self.RealPuzzle[i][j][0])

    def check_move(self, row, column, number):
        count = 0
        for j in range(9):
            if int(self.RealPuzzle[row-1][j][0]) == number and j!= column-1:
                count += 1
            if count > 0:
                self.RealPuzzle[row - 1][column - 1][1] = "red"

        count = 0
        for i in range(9):
            if int(self.RealPuzzle[i][column-1][0]) == number and i !=  row-1:
                count += 1
            if count > 0:
                self.RealPuzzle[row - 1][column - 1][1] = "red"
        count = 0
        for i in range(3):
            for j in range(3):
                if int(self.RealPuzzle[math.floor((row-1)/3)*3+i][math.floor((column-1)/3)*3+j][0]) == number and row-1 != math.floor((row-1)/3)*3+i and column-1 != math.floor((column-1)/3)*3+j:
                    count += 1
                if count > 0:
                    self.RealPuzzle[row - 1][column - 1][1] = "red"


'''

enum cellState
preExisting
wrong
correct

class cell
    value
    cellstate
'''