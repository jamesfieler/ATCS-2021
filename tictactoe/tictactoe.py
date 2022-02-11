import random
#from numpy import row_stack

class TicTacToe:
    def __init__(self):
        self.board = [[' ', '1', '2', '3'],['1', '-','-','-'],['2', '-','-','-'],['3', '-','-','-']]

    def print_instructions(self):
        print("Player 1 is \'X\' , Player 2 is \'O\'\nTake turns placing your pieces - the first to 3 in a row wins!")

    def print_board(self):
        for row in range(len(self.board)):
            print("\n")
            for col in range(len(self.board)):
                print(self.board[row][col], end="\t")
        print("\n")

    def is_valid_move(self, row, col):
        if self.board[row][col] == '-' and row <= len(self.board) and col <= len(self.board):
            return True
        return False

    def place_player(self, player, row, col):
        self.board[row][col] = player

    def take_manual_turn(self, player):
        row = int(input("Enter Row: "))
        col = int(input("Enter Column: "))
        if self.is_valid_move(row, col) == False:
            while self.is_valid_move(row, col) == False:
                print("Invalid - Enter New Move.")
                row = int(input("Enter Row: "))
                col = int(input("Enter Column: "))
        self.board[row][col] = player

    def take_random_turn(self, player):
        row = random.randint(1, len(self.board)-1)
        col = random.randint(1, len(self.board)-1)
        while self.is_valid_move(row, col) == False:
            row = random.randint(1, len(self.board)-1)
            col = random.randint(1, len(self.board)-1)
        self.board[row][col] = player
    
    def take_turn(self, player):
        print(f"Player {player}'s turn.")
        self.take_manual_turn(player)

    def check_single_col_win(self, col, player):
        for row in range(1, len(self.board)):
            if self.board[row][col] != player:
                return False
        return True
    def check_col_win(self, player):
        for col in range(1, len(self.board)):
            if self.check_single_col_win(col, player):
                return True
        return False

    def check_single_row_win(self, row, player):
        for col in range(1, len(self.board)):
            if self.board[row][col] != player:
                return False
        return True
    def check_row_win(self, player):
        for row in range(1, len(self.board)):
            if self.check_single_row_win(row, player):
                return True
        return False

    def check_diag_win(self, player):
        pos = neg = True
        row = col = 1
        for i in range(len(self.board)-1):
            if self.board[row][col] != player:
                pos = False
            row += 1
            col += 1
        row = 1
        col = len(self.board)-1
        for i in range(len(self.board)-1):
            if self.board[row][col] != player:
                neg = False
            row += 1
            col -= 1
        return pos or neg

    def check_win(self, player):
        return self.check_row_win(player) or self.check_col_win(player) or self.check_diag_win(player)

    def check_tie(self): # not able to assess possible future moves
        for row in range(1, len(self.board)):
            for col in range(1, len(self.board)):
                if self.board[row][col] == '-':
                    return False
        #return self.check_win('X') == False and self.check_win('O') == False
        return True

    def play_game(self):
        player1 = 'X'
        player2 = 'O'

        self.print_instructions()
        
        gameOver = False
        currentTurn = player1
        while gameOver == False:
            if self.check_win(player1):
                gameOver = True
                self.print_board()
                print("Player 1 Wins!")
            elif self.check_win(player2):
                gameOver = True
                self.print_board()
                print("Player 2 Wins!")
            elif self.check_tie():
                gameOver = True
                self.print_board()
                print("Tie!")
            else:
                self.print_board()
                #self.take_turn(currentTurn)
                if currentTurn == player1:
                    self.take_turn(player1)
                    currentTurn = player2
                else:
                    self.take_random_turn(player2)
                    currentTurn = player1