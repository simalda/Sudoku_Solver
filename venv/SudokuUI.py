MARGIN = 20
SIDE = 50
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
import math
import types
from  SudokuBoard import SudokuBoard
from  SudokuGame import SudokuGame
from  MiniBoard import MiniBoard
from Backtraking import Backtraking
from Mavoh import Mavoh

class SudokuUI(Frame):

    def __init__(self, parent, game = None, mav = None):
        self.miniBoardNum = 0
        Frame.__init__(self, parent, bg = "beige")
        self.parent = parent
        if(game != None):
            self.SetGame(game)
        self.row, self.column = 0,0
        self.mav = mav

        #self.__initUI()
        if(mav!= None):
            self.SetMavoh(mav)

    def SetGame(self, myGame):
        self.game = myGame
        if self.game.RealPuzzle == []:
            self.game.start()
        self.__initUI()

    def SetBoard(self):
        self.__initUI()

    def SetMavoh(self, m):
        self.mav = m
        #self.mav.mavoh = m.mavohGenerator()
        self.game = None
        self.__initUI()
        self.buttonM = Button(self, text="Solve Mavoh", command = self.mav.mavohSolver)
        self.buttonM.pack()
        self.buttonS = Button(self, text="Draw Solution", command = self.__draw_mavoh)
        self.buttonS.pack()

    def __draw_any_puzzle(self, puzzle):
        self.canvas.delete("numbers")
        if type(puzzle) is list:
            for i in range(9):
                for j in range(9):
                    if puzzle[i][j].value == 0:
                        self.__drawNumberinCell(i, j, '', self.ConvertToColor('incorrect'))
                    else:
                            self.__drawNumberinCell(i, j, puzzle[i][j].value, self.ConvertToColor( puzzle[i][j].cellState))
        else:
            for i in range(9):
                for j in range(9):
                    if puzzle.board[i][j].value == 0:
                        self.__drawNumberinCell(i, j, '',self.ConvertToColor('incorrect'))
                    else:
                        self.__drawNumberinCell(i, j, puzzle.board[i][j].value, self.ConvertToColor('incorrect'))

    def __draw_mavoh(self):
        self.canvas.delete("numbers")
        for i in range(9):
            for j in range(9):
                if self.mav.board[i][j] == '0':
                    self.canvas.create_text(MARGIN + SIDE / 2 + SIDE * j, MARGIN + SIDE / 2 + SIDE * i,
                                            tags="numbers", fill="black")
                else:
                    self.canvas.create_text(MARGIN + SIDE / 2 + SIDE * j, MARGIN + SIDE / 2 + SIDE * i, text = self.mav.board[i][j],
                                                tags="numbers", fill="black")

    def clear_answers(self):
        print(self.game.start_puzzle)
        self.__draw_any_puzzle(self.game.start_puzzleForGame)
        #self.game.RealPuzzle = self.game.start_puzzleForGame
        self.game.RealPuzzle = self.game.duplicate2(self.game.start_puzzleForGame)

    def show_solution(self):
        self.__draw_any_puzzle(self.game.solution)
        #  for child in self.winfo_children():
        #   child.configure(state='disable')
    def __draw_grid(self):
         for i in range(10):
             if i%3 ==0:
                 self.canvas.create_line(MARGIN, MARGIN + i * SIDE, SIDE * 9 + MARGIN, MARGIN + i * SIDE, fill="black")
             else:
                 self.canvas.create_line(MARGIN, MARGIN + i * SIDE, SIDE * 9 + MARGIN, MARGIN + i * SIDE, fill="gray")
         for i in range(10):
             if i % 3 == 0:
                 self.canvas.create_line(MARGIN + i * SIDE, MARGIN,  MARGIN + i * SIDE, SIDE * 9 + MARGIN, fill="black")
             else:
                 self.canvas.create_line(MARGIN + i * SIDE, MARGIN, MARGIN + i * SIDE , SIDE * 9 + MARGIN, fill="gray")
    def draw_puzzle(self):
        self.__draw_any_puzzle(self.game.RealPuzzle)

    def __draw_cursor(self):
        self.canvas.delete("cursor")
        self.canvas.create_rectangle(MARGIN+ (self.column-1) * SIDE,MARGIN+ (self.row-1) * SIDE,MARGIN+ self.column* SIDE, MARGIN+ self.row * SIDE, outline ="red", tags ="cursor")

    def __cell_clicked(self, event):
        self.canvas.focus_set()
        print(event.x, event.y)
        self.row = math.ceil((event.y-MARGIN)/SIDE)
        self.column = math.ceil((event.x - MARGIN) / SIDE)
        if MARGIN < event.x and event.x < MARGIN + SIDE * 9 and MARGIN < event.y and event.y < MARGIN + SIDE * 9 :
            self.__draw_cursor()
            self.__draw_miniBoard(event)

    def __draw_miniBoard(self, event):
        if self.miniBoardNum  == 0:
            self.miniBoardNum += 1
            def fuck(event):
                self.miniBoardNum -=1
            self.minBoard = MiniBoard(self.parent, callBack = self.SetNumber, onDestroy = fuck)

    def __key_pressed(self, event):
        print(event)
        print(self.game.start_puzzle.board[self.row-1][self.column-1])
        if  self.game.start_puzzle.board[self.row-1][self.column-1] == 0:
            self.game.RealPuzzle[self.row-1][self.column-1].value = event.char
            self.game.RealPuzzle[self.row - 1][self.column - 1].cellState = "correct"
            self.game.check_move(self.row, self.column, event.char)
            self.__draw_any_puzzle(self.game.RealPuzzle)
            print(self.game.check_win(self.game.RealPuzzle))
            if self.game.check_win(self.game.RealPuzzle):
                self.__draw_victory()

    def SetNumber(self, number):
        #print(self.game.start_puzzle.board[self.row-1][self.column-1])
        if  self.game.start_puzzleForGame[self.row-1][self.column-1].value == 0 :
            self.game.RealPuzzle[self.row-1][self.column-1].value = number
            self.game.RealPuzzle[self.row - 1][self.column - 1].cellState = "correct"
            self.game.check_board()
            self.game.check_move(self.row, self.column, number)
            self.__draw_any_puzzle(self.game.RealPuzzle)
            print(self.game.check_win(self.game.RealPuzzle))
            if self.game.check_win(self.game.RealPuzzle):
                self.__draw_victory()

    def __draw_victory(self):
        self.win = Toplevel(bg="beige")
        #self.win.wm_title("You WIN!!!!")
        self.win.geometry("250x150+300+100")
        self.win.attributes('-topmost', 1)
        #self.canvas.create_oval(100, 100, 440, 440, outline="red", fill="green", width=2)
        #self.canvas.create_text(239, 230, text="WIN", font=("Purisa", 86), fill="black")
        b = Button(self.win, text="YOU WIN!!!", command =  self.WINdestroy())
        b.pack(fill=X, relx=0.5, rely=0.5, anchor=CENTER)

    def WINdestroy(self):
        self.win.destroy()

    def  __initUI(self):
        self.text = Text(self)
        self.text.insert(INSERT, "Hello World\t")
        self.text.insert(END, "This is the first frame")
        self.canvas = Canvas(self, height = HEIGHT, width = WIDTH, bg ="beige")
        self.canvas.bind('<Button-1>', self.__cell_clicked)
        self.canvas.focus_set()
        self.canvas.bind('<Key>', self.__key_pressed)
        self.canvas.pack()
        self.button = Button(self, text="Clear answers ",command = self.clear_answers)
        self.button2 = Button(self, text="Show Solution", command=self.show_solution)
        self.button.pack()
        self.button2.pack()
        self.__draw_grid()
        if(self.game!= None):
            self.draw_puzzle()
        if(self.mav!= None):
            self.__draw_mavoh()

    def __drawExternalBoarder(self, left, up, right, down):
        self.canvas.create_line(self, left, up, right, down, fill="black")

    def __drawInternalBoarder(self, left, up, right, down):
        self.canvas.create_line(self, left, up, right, down, fill="gray")

    def __drawNumberinCell(self, i, j, text, fill):
        self.canvas.create_text(MARGIN + SIDE / 2 + SIDE * j, MARGIN + SIDE / 2 + SIDE * i,
                                text=text, tags="numbers", fill=fill)

    _colorDictionery = {"incorrect":"red", "correct":"green", "predefined" :"black"}
    def ConvertToColor(self, status):
        return self._colorDictionery [status]

