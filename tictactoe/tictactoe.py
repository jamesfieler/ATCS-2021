import random
import time

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

    def minimax(self, player, depth):
        if self.check_win('O'):
            return 10, None, None
        elif self.check_win('X'):
            return -10, None, None
        elif self.check_tie():
            return 0, None, None
        elif depth == 0:
            return 0, None, None
        
        opt_row = -1
        opt_col = -1
        if player == 'O':
            best = -10
            for row in range(1, len(self.board)):
                for col in range(1, len(self.board)):
                    if self.is_valid_move(row, col):
                        self.place_player('O', row, col)
                        score = self.minimax('X', depth-1)[0]
                        self.place_player('-', row, col)
                        if best < score:
                            opt_row = row
                            opt_col = col
                            best = score
            return best, opt_row, opt_col
        if player == 'X':
            worst = 10
            for row in range(1, len(self.board)):
                for col in range(1, len(self.board)):
                    if self.is_valid_move(row, col):
                        self.place_player('X', row, col)
                        score = self.minimax('O', depth-1)[0]
                        self.place_player('-', row, col)
                        if worst > score:
                            opt_row = row
                            opt_col = col
                            worst = score
            return worst, opt_row, opt_col

    def minimax_alpha_beta(self, player, depth, alpha, beta):
        if self.check_win('O'):
            return 10, None, None
        elif self.check_win('X'):
            return -10, None, None
        elif self.check_tie():
            return 0, None, None
        elif depth == 0:
            return 0, None, None
        
        opt_row = -1
        opt_col = -1
        if player == 'O':
            best = -10
            for row in range(1, len(self.board)):
                for col in range(1, len(self.board)):
                    if self.is_valid_move(row, col):
                        self.place_player('O', row, col)
                        score = self.minimax_alpha_beta('X', depth-1, alpha, beta)[0]
                        self.place_player('-', row, col)
                        if best < score:
                            opt_row = row
                            opt_col = col
                            best = score
                        if best < alpha:
                            alpha = best
                        if beta <= alpha:
                            return best, opt_row, opt_col
            return best, opt_row, opt_col
        if player == 'X':
            worst = 10
            for row in range(1, len(self.board)):
                for col in range(1, len(self.board)):
                    if self.is_valid_move(row, col):
                        self.place_player('X', row, col)
                        score = self.minimax_alpha_beta('O', depth-1, alpha, beta)[0]
                        self.place_player('-', row, col)
                        if worst > score:
                            opt_row = row
                            opt_col = col
                            worst = score
                        if worst > beta:
                            beta = worst
                        if beta <= alpha:
                            return worst, opt_row, opt_col
            return worst, opt_row, opt_col

    def take_minimax_turn(self, player, depth=9, alpha=None, beta=None):
        if alpha != None and beta != None:
            start = time.time()
            score, opt_row, opt_col = self.minimax_alpha_beta(player, depth, alpha, beta)
            end = time.time()
        else:
            start = time.time()
            score, opt_row, opt_col = self.minimax(player, depth)
            end = time.time()
        self.place_player(player, opt_row, opt_col)
        print(str(end - start) + "s")

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

    def check_tie(self): # not able to assess gaurenteed future tie
        for row in range(1, len(self.board)):
            for col in range(1, len(self.board)):
                if self.board[row][col] == '-':
                    return False
        return self.check_win('X') == False and self.check_win('O') == False

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
                if currentTurn == player1:
                    self.take_turn(player1)
                    currentTurn = player2
                else:
                    #self.take_turn(player2)
                    #self.take_random_turn(player2)
                    self.take_minimax_turn(player2, depth=10, alpha=-10, beta=10)
                    currentTurn = player1