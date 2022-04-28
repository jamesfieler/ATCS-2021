BOARD_WIDTH = 7
BOARD_HEIGHT = 6

def setBoard(width, height):
    board = []
    col = [' ']
    for i in range(width):
        col.append(str(i+1))
    board.append(col)
    for i in range(height):
        col = [str(i+1)]
        for j in range(width):
            col.append('-')
        board.append(col)
    return board

class ConnectFour:
    def __init__(self):
        self.board = setBoard(BOARD_WIDTH, BOARD_HEIGHT)

    def printBoard(self):
        for row in range(len(self.board)):
            print("\n")
            for col in range(len(self.board[0])):
                print(self.board[row][col], end="\t")
        print("\n")

    def validMove(self, row, col):
        if self.board[row][col] == '-' and row <= len(self.board) and col <= len(self.board):
            return True
        return False

    def userMove(self, player):
        row = int(input("Enter Row: "))
        col = int(input("Enter Column: "))
        if self.validMove(row, col) == False:
            while self.validMove(row, col) == False:
                print("Invalid - Enter New Move.")
                row = int(input("Enter Row: "))
                col = int(input("Enter Column: "))
        self.board[row][col] = player
    


c4 = ConnectFour()
c4.printBoard()
c4.userMove('X')
c4.printBoard()