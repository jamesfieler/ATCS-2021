import time
import random

def setBoard(width, height, blank):
    board = []
    col = ['#']
    for i in range(width):
        col.append(str(i+1))
    board.append(col)
    for i in range(height):
        col = [str(i+1)]
        for j in range(width):
            col.append(blank)
        board.append(col)
    return board

class ConnectFour:
    def __init__(self, width=7, height=6, blank='-', streak=4):
        self.WIDTH = width
        self.HEIGHT = height
        self.BLANK = blank
        self.STREAK=4
        self.board = setBoard(width, height, blank)

    def printBoard(self, outline=True):
        if outline:
            print("\n |", end="")
            for i in range(self.WIDTH+1):
                print("---|", end="")
            for row in range(self.HEIGHT+1):
                print("\n", "| ", end="")
                for col in range(self.WIDTH+1):
                    print(self.board[row][col], end=" | ")
                print("\n |", end="")
                for i in range(self.WIDTH+1):
                    print("---|", end="")
            print("\n")
        else:
            for row in range(len(self.board)):
                print("\n")
                for col in range(len(self.board)):
                    print(self.board[row][col], end="    ")
            print("\n")

    def nextRow(self, col):
        next = None
        if col > 0 and col < (self.WIDTH+1):
            for i in range (self.HEIGHT+1):
                if self.board[i][col] == self.BLANK:
                    next = i
        return next

    def takeTurn(self, player):
        col = input("Enter Column: ")
        while True:
            try:
                col = int(col)
                if self.nextRow(col) != None:
                    break
                else:
                    col = input("Invalid. Enter New Column: ")
            except:
                col = input("Invalid. Enter New Column: ")
        self.board[self.nextRow(col)][col] = player

    def takeComputerTurn(self, player, opponent, difficulty):
        if difficulty == 1:
            col = self.randomAlgorithm()
            self.board[self.nextRow(col)][col] = player
        elif difficulty == 2:
            col = self.heuristicAlgorithm(player, opponent)
            print("COLUMN: ", col)
            self.board[self.nextRow(col)][col] = player
        elif difficulty > 2 and difficulty < self.WIDTH*self.HEIGHT:
            col = self.minimax(player, player, opponent, difficulty)[1]
            self.board[self.nextRow(col)][col] = player
        else:
            raise Exception("Invalid Diffiuculty")
    
    def checkRowWin(self, player, streakSize):
        for row in range(1, self.HEIGHT+1):
            streak = 0
            for col in range(1, self.WIDTH+1):
                if self.board[row][col] == player:
                    streak += 1
                else:
                    streak = 0
                if streak >= streakSize:
                    return True
        return False
    
    def checkColWin(self, player, streakSize):
        for col in range(1, self.WIDTH+1):
            streak = 0
            for row in range(1, self.HEIGHT+1):
                if self.board[row][col] == player:
                    streak += 1
                else:
                    streak = 0
                if streak >= streakSize:
                    return True
        return False

    def checkDiagWin(self, player, streakSize):
        #positive slope diagonal
        for i in range(streakSize, self.HEIGHT+1): #top left half
            streak = 0
            for j in range(i+1):
                if self.board[i-j][1+j] == player:
                    streak += 1
                else:
                    streak = 0
                if streak >= streakSize:
                    return True
        for i in range(2, self.WIDTH-streakSize+1): #bot right half
            streak = 0
            for j in range(self.WIDTH-i+1):
                if self.board[self.HEIGHT-j][i+j] == player:
                    streak += 1
                else:
                    streak = 0
                if streak >= streakSize:
                    return True

        #negative slope diagonal
        for i in range(1, self.HEIGHT-streakSize+2): #bot left half
            streak = 0
            for j in range(self.HEIGHT-i+1):
                if self.board[i+j][1+j] == player:
                    streak += 1
                else:
                    streak = 0
                if streak >= streakSize:
                    return True
        for i in range(2, self.WIDTH-streakSize+2): #top right half
            streak = 0
            for j in range(self.WIDTH-i+1):
                if self.board[1+j][i+j] == player:
                    streak += 1
                else:
                    streak = 0
                if streak >= streakSize:
                    return True
        return False

    def checkTie(self):
        for row in range(1, self.HEIGHT+1):
            for col in range(1, self.WIDTH+1):
                if self.board[row][col] != self.BLANK:
                    return False

    def checkWin(self, player):
        return self.checkRowWin(player, self.STREAK) or self.checkColWin(player, self.STREAK) or self.checkDiagWin(player, self.STREAK)

    def randomAlgorithm(self):
        move = random.randint(1, self.WIDTH+1)
        while self.nextRow(move) == None:
            move = random.randint(1, self.WIDTH+1)
        return move

    def winningMoves(self, player):
        for col in range(1, self.WIDTH+1):
            nextRow = self.nextRow(col)
            if nextRow != None:
                self.board[nextRow][col] = player
                if self.checkWin(player):
                    self.board[nextRow][col] = self.BLANK
                    return col
                self.board[nextRow][col] = self.BLANK #can [] be null?
        return None

    def heuristicAlgorithm(self, player, opponent):
        move = self.winningMoves(player)
        if move != None:
            return move
        move = self.winningMoves(opponent)
        if move != None:
            return move

        for col in range(2, self.WIDTH-2):
            if self.board[self.HEIGHT][col] == opponent and self.board[self.HEIGHT][col+1] == self.BLANK and self.board[self.HEIGHT][col+2] == opponent:
                return col+1

        losingMoves = []
        for col in range(1, self.WIDTH+1):
            nextRow = self.nextRow(col)
            if nextRow != None:
                self.board[nextRow][col] = player
                if self.winningMoves(opponent) != None:
                    losingMoves.append(col)
                self.board[nextRow][col] = self.BLANK

        #print("LOSING MOVES: ", losingMoves)
        #print("POSITION")
        for i in range(1, 4):
            move = int(self.WIDTH/2) + 1
            if move not in losingMoves:
                nextRow = self.nextRow(move)
                if nextRow != None:
                    if nextRow > self.HEIGHT-1-i:
                        print("1")
                        return move
            move = int(self.WIDTH/2)
            if move not in losingMoves:
                nextRow = self.nextRow(move)
                if nextRow != None:
                    if nextRow > self.HEIGHT-i+1:
                        print("4")
                        return move
            move = int(self.WIDTH/2) + 2
            if move not in losingMoves:
                nextRow = self.nextRow(move)
                if nextRow != None:
                    if nextRow > self.HEIGHT-i+1:
                        print("4")
                        return move
            move = int(self.WIDTH/2) - 1
            if move not in losingMoves:
                nextRow = self.nextRow(move)
                if nextRow != None:
                    if nextRow > self.HEIGHT-i:
                        print("2")
                        return move
            move = int(self.WIDTH/2) + 3
            if move not in losingMoves:
                nextRow = self.nextRow(move)
                if nextRow != None:
                    if nextRow > self.HEIGHT-i:
                        print("3")
                        return move

        #print("RANDOM")
        if len(losingMoves) > self.WIDTH:
            move = self.randomAlgorithm
        else:
            move = self.randomAlgorithm()
            while move in losingMoves:
                move = self.randomAlgorithm()
        return move
    
    def minimax(self, player, player1, player2, depth):
        if self.checkWin('O'):
            return (10, None)
        elif self.checkWin('X'):
            return (-10, None)
        elif self.checkTie():
            return (0, None)
        elif depth == 0:
            return (0, None)
        
        optMove = -1
        if player == player1:
            best = -100
            for col in range(1, self.WIDTH+1):
                next = self.nextRow(col)
                if next != None:
                    self.board[next][col] = player1
                    score = self.minimax(player2, player1, player2, depth-1)[0]
                    self.board[next][col] = self.BLANK
                    if best < score:
                        optMove = col
                        best = score
            return best, optMove
    
        if player == player2:
            worst = 100
            for col in range(1, self.WIDTH+1):
                next = self.nextRow(col)
                if next != None:
                    self.board[next][col] = player2
                    score = self.minimax(player1, player1, player2, depth-1)[0]
                    self.board[next][col] = self.BLANK
                    if worst > score:
                        optMove = col
                        worst = score
            return worst, optMove

    def playGame(self, player1='X', player2='O', opponent='user', difficulty=2, min_move_time=0):
        gameOver = False
        currentTurn = player1
        while gameOver == False:
            if self.checkWin(player1):
                gameOver = True
                self.printBoard()
                print("Player 1 Wins!")
            elif self.checkWin(player2):
                gameOver = True
                self.printBoard()
                print("Player 2 Wins!")
            elif self.checkTie():
                gameOver = True
                self.printBoard()
                print("Tie!")
            else:
                self.printBoard()
                if currentTurn == player1:
                    self.takeTurn(player1)
                    currentTurn = player2
                else:
                    if opponent == 'user':
                        self.takeTurn(player2)
                    elif opponent == 'computer':
                        self.takeComputerTurn(player2, player1, difficulty)
                        time.sleep(min_move_time)
                        currentTurn = player1
                    else:
                        raise Exception("Invalid Opponent")


