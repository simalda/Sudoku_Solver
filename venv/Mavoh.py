from Backtraking import Backtraking

class Mavoh(object):

    def __init__(self, stuckPath = [], been = [], board = [], mavohBusyCells = []):
        self.stuckPath = stuckPath
        self.been = been
        #self.mavoh = mavoh
        self.mavohBusyCells = mavohBusyCells
        self.board = self.mavohGenerator()

    def mavohGenerator(self):
        b = Backtraking()
        n = 0
        for n in range(25):
            i, j = b.RandCoor()
            if (i != 0  or j != 0) and (i != 8  or j != 8):
                b.board[i][j] ='1'
                n += 1
                self.mavohBusyCells.append(Pair(i,j))
        resut = self.superToString(self.mavohBusyCells)
        #print(resut)
        return b.board

    def mavohSolver(self):
        self.board[0][0] = '*'
        firstElem = Pair(0,0)
        lastElem = Pair(8,8)
        nonMove = Pair(-1,-1)
        self.stuckPath.append(firstElem)
        self.been.append(firstElem)

        nextMove = Pair(self.getNextMove().a, self.getNextMove().b)
        while(self.stuckPath[-1]!= lastElem and (self.stuckPath[-1] != firstElem or len(self.stuckPath) != 1 or nextMove != nonMove)):
        #for i in range(3):

            if( nextMove != nonMove):
               self.stuckPath.append(nextMove)
               self.been.append(nextMove)
               resut = self.superToString(self.stuckPath)
               #print(resut)
               self.board[self.stuckPath[-1].a][self.stuckPath[-1].b] = '*'

            else:
                if len(self.stuckPath) > 1:
                    self.stuckPath.pop(-1)
            #print(self.stuckPath)
            nextMove = Pair(self.getNextMove().a, self.getNextMove().b)

    def superToString(self, x):
        result = ""
        result += "["
        for thing in x:
            result += "{}".format(thing)
            result += ","

        result += "]"

        return result

    def getNextMove(self):
        a1 = Pair(0,1)
        a2 = Pair(1,0)
        a3 = Pair(0,-1)
        a4 = Pair(-1, 0)
        n = Pair(-1,-1)
        steps = [a1, a2, a3, a4]
        for i in range(len(steps)):
            next = self.stuckPath[-1] + steps[i]
            if next.a >= 0 and next.a <= 8 and next.b >= 0 and next.b <= 8:
                if (next  not in self.been) and (next not in self.stuckPath) and (next not in self.mavohBusyCells):
                    return next
        return n


    def draw_solution(self):
        for i in range(len(self.stuckPath)):
            b.board[self.stuckPath[i][0]][self.stuckPath[i][1]] =='*'
        return b.board



class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self,other):
        c = Pair(self.a+other.a, self.b+other.b)
        return c

    def __str__(self):
        return '({}, {})'.format(self.a, self.b)

    def __eq__(self,other):
        return (self.a == other.a and  self.b == other.b)

    def __ne__(self, other):
        return not self.__eq__(other)