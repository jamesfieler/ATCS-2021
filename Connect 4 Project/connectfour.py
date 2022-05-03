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

    def nextRow(self, col):
        next = None
        if col > 0 and col < len(self.board[0]):
            for i in range(len(self.board)):
                if self.board[i][col] == '-':
                    next = i
        return next

    def takeMove(self, player):
        col = int(input("Enter Column: "))
        if self.nextRow(col) == None:
            while self.nextRow(col) == None:
                col = int(input("Invalid. Enter New Column: "))
        self.board[self.nextRow(col)][col] = player



c4 = ConnectFour()
for i in range(42):
    c4.printBoard()
    c4.takeMove('X')
c4.printBoard()