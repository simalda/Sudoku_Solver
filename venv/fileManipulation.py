from  SudokuBoard import SudokuBoard
from  SudokuGame import SudokuGame
from  SudokuUI import SudokuUI
from tkinter.filedialog import *

class fileManipulation(object):
    def new_game(app):
        game1 = SudokuGame("SudokuBoard.txt")
        return game1


        #sudUI = SudokuUI(app ,game1)
        #sudUI.__init__(app, game1)
        
        
    def file_load(app):
        file_path = askopenfilename()
        print(file_path)
        loaded_game = SudokuGame('',file_path)
        return loaded_game

    
    def file_save(app):
        self.parent.f = asksaveasfile(mode='w', defaultextension=".txt")
        if self.parent.f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
            return
        text2save = ''
        for i in range(9):
            for j in range(9):
                text2save += str(self.game.RealPuzzle[i][j][0])
            text2save += '\n'
        #text2save = str(self.game.RealPuzzle)  # starts from `1.0`, not `0.0`
        self.parent.f.write(text2save)
        self.parent.f.close()