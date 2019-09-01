from tkinter import *
from SudokuBoard import SudokuBoard
from SudokuGame import SudokuGame
from SudokuUI import SudokuUI
from fileManipulation import *
from Backtraking import Backtraking
from Mavoh import Mavoh
from Language import *
from center import center


class App(object):
    def __init__(self):
        self.app = Tk()
        self.screen_width = self.app.winfo_screenwidth()
        self.screen_height = self.app.winfo_screenheight()
        self.lang = Language('English')
        self.sudUI = SudokuUI(self.app)
        #self.menu = self.SetupMenu()
        self.app.title("sudoku")
        self.app.iconbitmap(r'C:/Users/simal/repos/Sudoku_Solver/a.ico')
        self.app.geometry("650x650+300+50")
        self.popup_showinfo()

        #self.app.configure(menu=self.menu)



    def Go(self):
        self.sudUI.pack(fill=X)
        self.app.mainloop()

    def SetupMenu(self):
        menu = Menu(self.app, tearoff=False)
        subMenu = Menu(menu, tearoff=False)
        subSubMenu = Menu(subMenu, tearoff=False)
        #№menu.add_cascade(label="File", underline=0, menu = subMenu)
        menu.add_cascade(label =  self.lang.File, underline=0, menu=subMenu)
        subMenu.add_cascade(label= self.lang.NewGame, menu=subSubMenu, underline=0)
        subSubMenu.add_command(label=self.lang.Easy, command = lambda level ='Easy': self.newGame(level))
        subSubMenu.add_command(label=self.lang.Medium, command = lambda level ='Medium': self.newGame(level))
        subSubMenu.add_command(label= self.lang.Hard , command  = lambda level ='Hard': self.newGame(level))
        subMenu.add_command(label=self.lang.LoadGame, command=self.load)
        subMenu.add_command(label=self.lang.ChoseYourLanguage, command=self.popup_showinfo)
        subMenu.add_command(label=self.lang.SaveGame, command=self.save, state=DISABLED)
        subMenu.add_command(label=self.lang.ClearAnswers, command=self.sudUI.clear_answers, state=DISABLED)
        subMenu.add_command(label=self.lang.ShowSolution, command=self.sudUI.show_solution, state=DISABLED)
        #subMenu.add_command(label="zibi", command=self.zibi)
        self.app.config(menu=menu)
        return menu

    def EnableMenu(self):
        self.menu.winfo_children()[0].entryconfig(self.lang.ClearAnswers, state=NORMAL)
        self.menu.winfo_children()[0].entryconfig(self.lang.SaveGame, state=NORMAL)
        self.menu.winfo_children()[0].entryconfig(self.lang.ShowSolution, state=NORMAL)

    def zibi(self):
        if not hasattr(self,"zibi"):
            self.zibi = TRUE

        self.zibi = not self.zibi
        self.menu.winfo_children()[0].entryconfig("zibi", background="YELLOW"if self.zibi else "GREEN" )

    def newGame(self, level):
        self.Clear()
        self.EnableMenu()
        self.CreateGame(level)


    def load(self):
        self.fMan = fileManipulation(self.app)
        self.Clear()
        self.EnableMenu()
        self.fMan.file_load( self.sudUI)



    def save(self):
        self.fMan = fileManipulation(self.app)
        self.fMan.file_save2(self.sudUI)

    def Clear(self):
        if self.sudUI.children.__len__() != 0:
            self.sudUI.canvas.destroy()
            self.sudUI.button.destroy()
            self.sudUI.button2.destroy()

    def CreateGame(self, level):
        game = SudokuGame(level)
        self.sudUI.SetGame(game)



    def popup_showinfo(self):
        self.wind = Toplevel(bg = "beige")
        self.wind.wm_title("Sudoku lang")
        self.wind.geometry("250x150+"+str(int(self.screen_width/2))+'+'+str(int(self.screen_height/2)))

        self.wind.attributes('-topmost', 1)

       # photo = PhotoImage(file = 'C:/Users/simal/repos/Sudoku_Solver/purple.ico')
        #label= Label(self.win, image = photo)
        #label.pack()


        l = Label(self.wind, text="Chose Your Language",bg = "beige")
        l.pack(fill=X,pady=10, anchor =CENTER)

        for language in self.lang.langDict:
            b = Button(self.wind, text=language, command=lambda lan=language:    self.setLanguage(lan))
            b.pack(fill=X, pady=5)



        self.wind.bind("<Destroy>", self._destroy)
    def _destroy(self, event):
        self.menu = self.SetupMenu()
            # b3 = Button(self.wind, text="עברית", command = lambda lan ='עברית': self.setLanguage(lan) )
            # b3.pack(fill=X,pady=5)



    def setLanguage(self,langu):
        self.lang = Language(langu)
        self.menu = self.SetupMenu()
        self.sudUI.lang = self.lang
        self.wind.destroy()


def main():
    myApp = App()
    myApp.Go()

if __name__== "__main__":
     main()