class Board:

    

    def __init__(self,board = None):
        self._board = []        
        if board is None:
            self._board = [[' '] * 8 for _ in range(8)]
        else:                   
            self._board = [[' ' for j in range(8)] for i in range(8)]
            for x in range(8):
                for y in range(8):
                    self._board[x][y] = board[x][y]

    def resetBoard(self):
        
        self._board = [[' ' for j in range(8)] for i in range(8)]

        
        self._board[3][3] = 'X'
        self._board[3][4] = 'O'
        self._board[4][3] = 'O'
        self._board[4][4] = 'X'

    def getBoardCopy(self): 
        return self._board[:][:]

    def getValidMoves(self,tile):
        
        return [[x,y] for y in range(8) for x in range(8) if self.isValidMove(tile, x, y)]

    def isValidMove(self, tile, xStart, yStart):
        
        if self._board[xStart][yStart] != ' ' or not self.isOnBoard(xStart, yStart):
            return False

        self._board[xStart][yStart] = tile  

        if tile == 'X':
            otherTile = 'O'
        else:
            otherTile = 'X'

        tilesToFlip = []
        for xDirection, yDirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
          
            x, y = xStart, yStart
            x += xDirection  
            y += yDirection
            if self.isOnBoard(x, y) and self._board[x][y] == otherTile:
               
                x += xDirection
                y += yDirection
                if not self.isOnBoard(x, y):
                    continue
                while self._board[x][y] == otherTile:
                    x += xDirection
                    y += yDirection
                    if not self.isOnBoard(x, y):
                        break
                if not self.isOnBoard(x, y):
                    continue
                if self._board[x][y] == tile:
                    
                    while True:
                        x -= xDirection
                        y -= yDirection
                        if x == xStart and y == yStart:
                            break
                        tilesToFlip.append([x, y])

        self._board[xStart][yStart] = ' '  
        if len(tilesToFlip) == 0:  
            return False
        return tilesToFlip

    def isOnBoard(self, x, y):
        
        return 0 <= x <= 7 and 0 <= y <= 7

    def isOnCorner(self, x, y):
        
        return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)

    def getElement(self, x ,y):
        
        return self._board[x][y]

    def getScoreOfBoard(self):
        
        xScore = 0
        oScore = 0
        for x in range(8):
            for y in range(8):
                if self._board[x][y] == 'X':
                    xScore += 1
                if self._board[x][y] == 'O':
                    oScore += 1
        return {'X': xScore, 'O': oScore}

    def makeMove(self, tile, xStart, yStart):
        

        tilesToFlip = self.isValidMove(tile, xStart, yStart)

        if tilesToFlip == False:
            return False

        self._board[xStart][yStart] = tile
        for x, y in tilesToFlip:
            self._board[x][y] = tile  
        return True

    def setFake(self):  
        self._board = [
            ['X', 'O', 'X', 'X', 'X', 'X', 'X', 'X'],
            ['O', 'O', '0', 'X', 'O', 'X', 'X', 'X'],
            ['X', 'O', 'X', 'X', 'X', 'O', 'X', 'X'],
            ['X', 'O', 'O', 'O', 'X', 'X', 'X', 'X'],
            ['X', 'O', 'O', 'X', 'O', 'O', 'X', 'X'],
            ['X', 'O', 'X', 'X', 'X', 'X', 'O', 'X'],
            ['X', 'X', 'X', 'X', 'X', 'O', ' ', ' '],
            ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
        ]
        for i in range(8):
            for j in range(i+1, 8):
                self._board[i][j], self._board[j][i] = self._board[j][i], self._board[i][j]