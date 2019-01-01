from tkinter import *
from SudokuBoard import SudokuBoard
from SudokuGame import SudokuGame
from SudokuUI import SudokuUI
from fileManipulation import *
from Backtraking import Backtraking
from Mavoh import Mavoh


class App(object):
    def __init__(self):
        self.app = Tk()
        self.sudUI = SudokuUI(self.app)
        self.SetupMenu()
        self.app.title("sudoku")
        self.app.geometry("650x650+300+100")

    def Go(self):
        self.sudUI.pack()
        self.app.mainloop()

    def SetupMenu(self):
        menu = Menu(self.app, tearoff=False)
        subMenu = Menu(menu, tearoff=False)
        subSubMenu = Menu(subMenu, tearoff=False)
        menu.add_cascade(label="File", underline=0, menu = subMenu)
        subMenu.add_cascade(label='New Game', menu=subSubMenu, underline=0)
        subSubMenu.add_command(label="Easy", command=self.easy)
        subSubMenu.add_command(label="Medium", command=self.medium)
        subSubMenu.add_command(label="Hard", command=self.hard)
        subMenu.add_command(label="Load Game", command=self.load)
        subMenu.add_command(label="Save Game", command=self.save)
        subMenu.add_command(label="Clear Answers", command=self.sudUI.clear_answers)
        subMenu.add_command(label="Show Solution", command=self.sudUI.show_solution)
        self.app.config(menu=menu)

    def easy(self):
        self.Clear()
        self.CreateGame('easy')

    def medium(self):
        self.Clear()
        self.CreateGame('medium')

    def hard(self):
        self.Clear()
        self.CreateGame('hard')

    def load(self):
        self.Clear()
        self.sudUI.SetGame(fileManipulation.file_load(app))

    def save(self):
        self.sudUI.SetGame(fileManipulation.file_save(app))

    def Clear(self):
        if self.sudUI.children.__len__() != 0:
            self.sudUI.canvas.destroy()
            self.sudUI.button.destroy()

    def CreateGame(self, level):
        game = SudokuGame(level)
        self.sudUI.SetGame(game)

def main():
    myApp = App()
    myApp.Go()

if __name__== "__main__":
     main()