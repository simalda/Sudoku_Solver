from tkinter import *
import math
import SudokuUI

class MiniBoard(Toplevel):
    SIDE = SudokuUI.SIDE
    def __init__(self, parent, callBack, onDestroy = None, number = 0, hint=0):
        Toplevel.__init__(self, parent)
        self.callBack = callBack
        self.onDestroy = onDestroy
        self.__draw_miniBoard()
        self.number = number
        self.hint = hint

        def _delete_window():
            print("delete_window")
            self.destroy()


        def _internalDestroy(event):
            if (event.widget == self):
                self.onDestroy(event)

        self.wm_protocol("WM_DELETE_WINDOW", _delete_window)
        if (self.onDestroy != None):
            self.bind("<Destroy>", _internalDestroy)



    def __draw_miniBoard(self):
        self.myFrame = Frame(self, bg="gray")
        x = self.winfo_pointerx()
        y = self.winfo_pointery()
        self.geometry("156x156+"+ str(x)+"+"+str(y))
        self.canvas2 = Canvas(self.myFrame, height = self.SIDE*3 , width = self.SIDE*3 , bg="azure")
        self.canvas2.bind('<Button-1>', self.click)
        self.canvas2.focus_set()
        self.canvas2.pack()
        self.myFrame.pack()
        for i in range(3):
            self.canvas2.create_line(i *  self.SIDE , 0, i * self.SIDE , self.SIDE * 3 , fill="black")
        for i in range(3):
            self.canvas2.create_line(0,  i * self.SIDE , self.SIDE * 3 , i * self.SIDE , fill="black")
        for i in range(3):
            for j in range(3):
                self.canvas2.create_text(self.SIDE / 2 + self.SIDE * j, self.SIDE / 2 + self.SIDE * i, tags="numbers", fill="black", text = 3*i+j+1)
        self.myFrame.grab_set()

    def click(self, event):
        number = self.__miniBoard_clicked(event)
        self.callBack(number, self.hint)
        self.destroy()

    def __miniBoard_clicked(self, event):
        row = math.ceil((event.y - 2) / self.SIDE)
        column = math.ceil((event.x - 2) / self.SIDE)
        number = 3 * (row-1) + column
        return number
