from  SudokuBoard import SudokuBoard
from  SudokuGame import SudokuGame
from  SudokuUI import SudokuUI
from tkinter.filedialog import *
from Cell import Cell
import json
import ast

class fileManipulation(object):

    def __init__(self, app ):
        self.app =app


    def file_load(self, app):
        f =   askopenfile(mode="r")
        try:
            if f != False:
                lines = f.read().splitlines()
                realPazGame = self.CreatePuz(lines, 0, 8)
                solPazGame = self.CreatePuz(lines, 10, 18)
                startPaz = []
                for i in range(9):
                    x = []
                    for j in range(9):
                        if realPazGame[i][j].cellState != 'predefined':
                            newCell = Cell(0, 'predefined', '')
                            x.append(newCell)
                        else:
                            newCell = Cell(realPazGame[i][j].value, realPazGame[i][j].cellState, set())
                            x.append(newCell)
                    startPaz.append(x)

                gamee = SudokuGame('', '', realPazGame, solPazGame, startPaz, startPaz)
                app.SetGame(gamee)



        except:
            self.__draw_ex(app)
        finally:
            if f in locals():
                f.close()


    def __draw_ex(self, ap):
        self.app.win = Toplevel(bg="beige")
        self.app.win.geometry("250x150+300+100")
        self.app.win.attributes('-topmost', 1)
        b = Button(self.app.win, text="Can not parse file!!!", command = self.WINdestroy)
        b.pack(fill=X, pady=5, anchor = CENTER)

    def WINdestroy(self):
        self.app.win.destroy()


    def CreatePuz(self, lines, fromRow, toRow):
        boardStr = ''
        for i in range(fromRow, toRow):
            boardStr += str(lines[i]) + ','
        boardStr += str(lines[toRow])
        boardPaz = list(ast.literal_eval(boardStr))
        return self.fromListToBoard(boardPaz)


    def fromListToBoard(self, boardList):
        puzzle =[]
        for i in range(9):
            x = []
            for j in range(9):
                newCell = Cell(boardList[i][j][0], boardList[i][j][1], set())
                x.append(newCell)
            puzzle.append(x)
        return puzzle





    def saveBoard(self, board, solution):
        text2save=''
        for i in range(9):
            for j in range(9):
                text2save += str(board[i][j])
            text2save += '\n'
        text2save += '*\n'
        for i in range(9):
            for j in range(9):
                text2save += str(solution[i][j])
            text2save += '\n'
        return text2save
    
    def file_save(self, app):
        f = asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
            return
        text2save = ''
        text2save += self.saveBoard(app.game.RealPuzzle, app.game.solution)
        #text2save = str(self.game.RealPuzzle)  # starts from `1.0`, not `0.0`
        f.write(text2save)
        f.close()

    def file_save2(self, app):
        f = asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
            return

        listOfTwo =[]

        listRealPuzToSave =[]

        for i in range(9):
            x=[]
            for j in range(9):
                newList =[app.game.RealPuzzle[i][j].value, app.game.RealPuzzle[i][j].cellState]
                x.append(newList)
            listRealPuzToSave.append(x)

        listSolPuzToSave = []

        for i in range(9):
            x = []
            for j in range(9):
                newList = [app.game.solution[i][j].value, app.game.solution[i][j].cellState]
                x.append(newList)
            listSolPuzToSave.append(x)

        for item in listRealPuzToSave:
            f.write("%s\n" % item)
        f.write('*\n')
        for item in listSolPuzToSave:
            f.write("%s\n" % item)
        f.close()

