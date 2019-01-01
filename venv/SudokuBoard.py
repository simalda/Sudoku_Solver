from Backtraking import Backtraking

 
    """
    Sudoku Board representation
    """
    def __init__(self, level, board_file='', solution =[]):
        self.solution = solution
        if board_file!='':
            self.board = self.__load_board(board_file)
        else:
            self.board, self.solution = self.__create_board(level)

        #init self.board using __create_board function
    def __create_board(self, level):
        b =  Backtraking()
        b.sudokuSolver(level)
        return b.board, b.solution

    def __load_board(self, board_file):
        board = []
        f = open(board_file, "r+")
        for i in range(9):
            board.append(list(f.readline().strip('\n')))
        f.close()
        return board