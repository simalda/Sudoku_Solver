import unittest
from  SudokuBoard import SudokuBoard
from  SudokuGame import SudokuGame
from  SudokuUI import SudokuUI



class TestSudoku(unittest.TestCase):

    # def test__(self):
    #   self.assertEqual('foo'.upper(), 'FOO')

    def test__check_winIncorrect(self):
        gameBoard = SudokuGame("SudokuBoard.txt")
        puzzle = []
        for i in range(9):
            x = []
            for j in range(9):
                x.append([gameBoard.start_puzzle.board[i][j], "black"])
            puzzle.append(x)
        self.assertFalse(gameBoard.check_win(puzzle))


    def test__check_winCorrect(self):
        gameBoard = SudokuGame("SudokuBoard.txt")
        puzzle = []
        for i in range(9):
            x = []
            for j in range(9):
                x.append([gameBoard.start_puzzle.board[i][j], "black"])
            puzzle.append(x)
        self.assertFalse(gameBoard.check_win(puzzle))

    def test__check_winCorrect(self):
        gameBoard = SudokuGame("WinBoard.txt")
        puzzle = []
        for i in range(9):
            x = []
            for j in range(9):
                x.append([gameBoard.start_puzzle.board[i][j], "black"])
            puzzle.append(x)
        self.assertRaises(TypeError,gameBoard.check_win(puzzle))
    # def test__key_pressed(self):
    # self.assertRaises(ValueError,,'h'):


if __name__ == '__main__':
    unittest.main()