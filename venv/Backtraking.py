import random
import math
from Cell import *

class Backtraking(object):
    def __init__(self, board =[], pathStuck = [], been = [], S = [], solution = []):
        self.board = board
        self.solution =solution
        self.emptyBoard()
        self.pathStuck = pathStuck
        self.been = been
        self.S = S

    def emptyBoard(self):
        self.board=[]
        for i in range(9):
            x = []
            for j in range(9):
                x.append('')
            self.board.append(x)
        print(self.board)

    def backForNumber(self, number):
        counter = 0
        S = [1,2,3,4,5,6,7,8,9]
        S.remove(number)
        leftRow = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        leftColumn = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        while(counter!=9):

            i, j = self.RandCoor2(counter, leftRow, leftColumn)

            while self.board[i][j]!= '':
                i, j = self.RandCoor2(counter, leftRow, leftColumn)

            if self.check_numberinRow(number, i) and self.check_numberinColumn(number, j) and self.check_numberinSquare(number, i, j):
                self.board[i][j] = number
                self.pathStuck.append((i,j,number))
                a = M((i,j,number),S)
                self.been.append(a)
                counter += 1
                leftRow.remove(i)
                leftColumn.remove(j)
                print(i,j)
        print(self.board)

    def findEmptyCell(self):
        for i in range(9):
            for j in range (9):
                if self.board[i][j] == '':
                    return i,j
        return -7, -7

    def RandCoor(self):
        return  random.randrange(0, 9, 1), random.randrange(0, 9, 1)

    def RandCoor2(self, counter, leftRow, leftColumn):
        print(type(counter))
        a = 9 - counter
        i = leftRow[random.randrange(0, a, 1)]
        j = leftColumn[random.randrange(0, a, 1)]
        return  i, j

    def RandCoor3(self):
        return  random.randrange(1, 10, 1)

    def check_numberinRow(self, number, row):
        if number in self.board[row]:
            return False
        return True

    def check_numberinColumn(self, number, column):
        for i in  range(9):
            if number == self.board[i][column]:
                return False
        return True

    def check_numberinSquare(self, number, row, column):
        square = []
        for i in range(3):
            for j in range(3):
                square.append(self.board[math.floor(row/3)*3 + i][math.floor(column/3)*3 + j])
        if number in square:
            return False
        return True

    def countSforCell(self, i, j):
        Scell = []
        Srow = self.countNOTSforRow(i)
        Scolumn = self.countNOTSforColumn(j)
        Ssquare = self.coountNOTSforSquare(i, j)
        for i in range(1,10,1):
            if (i not in Srow) and (i not in Scolumn) and (i not in Ssquare):
                Scell.append(i)
        return Scell

    def countNOTSforColumn(self, j):
        sr = []
        for k in range(9):
          sr.append(self.board[k][j])
        return sr

    def countNOTSforRow(self, i):
        sc = []
        for k in range(9):
          sc.append(self.board[i][k])
        return sc

    def coountNOTSforSquare(self, row, column):
        ss=[]
        for i in range(3):
            for j in range(3):
                ss.append(self.board[math.floor(row/3)*3 + i][math.floor(column/3)*3 + j])
        return ss

    def sudokuSolver(self, level):
        num = self.RandCoor3()
        self.backForNumber(num)
        i, j = self.findEmptyCell()
        self.S = self.countSforCell(i, j)
        #print(self.S)
        nextMove = self.S[random.randrange(0, len(self.S), 1)]

        while self.board[8][8] == '' or self.board[8][7] == '':
            if self.S != []:
                self.board[i][j] = nextMove
                self.pathStuck.append((i,j,nextMove))
                a = M((i, j, nextMove), self.S)
                self.been.append(a)
                #print(self.pathStuck)
                i, j = self.findEmptyCell()
                self.S = self.countSforCell(i, j)

            else:
                while self.S == []:
                    self.board[self.pathStuck[-1][0]][self.pathStuck[-1][1]] = ''
                    self.pathStuck.pop(-1)
                    self.been[-1].optionsForCell.remove(self.been[-1].cell[2])
                    self.S = self.been[-1].optionsForCell
                    self.been.pop(-1)
                    #print(self.pathStuck)
                    #print(self.S)

                i, j = self.findEmptyCell()
                print(self.pathStuck)
            print(self.S)
            if len(self.S) > 0:
                nextMove = self.S[random.randrange(0, len(self.S), 1)]
        self.solution = self.configBoard(self.board)

        if level =='Easy':
            self.SetLevel(1)
        if level =='Medium':
            self.SetLevel(4)
        if level =='Hard':
            self.SetLevel(7)

    def configBoard(self, board):#?????
        confiBoard=[]
        for i in range(9):
            x = []
            for j in range(9):
                x.append(Cell(self.board[i][j], "predefined",set()))
            confiBoard.append(x)
        return confiBoard

    def SetLevel(self,numofEmptycells):
        for i in range(9):
            rowToClear = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for k in range(numofEmptycells):
                j = random.randrange(0, len(rowToClear), 1)
                self.board[i][j] = 0
                rowToClear.remove(rowToClear[j])
        self.board = self.configBoard(self.board)


class M(object):
    def __init__(self, cell, optionsForCell):
        self.cell = cell
        self.optionsForCell = optionsForCell
