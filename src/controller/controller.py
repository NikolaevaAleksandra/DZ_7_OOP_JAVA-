import random

from src.model.model import Board
from src.view.view import View
from src.ai.ai import Ai


class Controller:
    

    def __init__(self): 
        self._viewer = View()
        self._ai = Ai()

    def whoGoesFirst(self): 
        if random.randint(0, 1) == 0: 
            return 'computer'
        else:
            return 'player'

    def run(self):  
        self._viewer.hi()
        ex = False
        while not ex:
            mainBoard = Board()
            mainBoard.resetBoard()  
                                    
            playerTile, computerTile = self._viewer.enterPlayerTile() 
            turn = self.whoGoesFirst() 
            self._viewer.printFirstTurn(turn)
            endGame = False

            while not endGame:
                if turn == 'player':
                    
                    if self._viewer.showHints:
                        validMoves = mainBoard.getValidMoves(playerTile) 
                        self._viewer.drawBoard(mainBoard, validMoves)
                    else:
                        self._viewer.drawBoard(mainBoard)
                    self._viewer.showPoints(mainBoard, playerTile, computerTile) 
                    move = self._viewer.getPlayerMove(mainBoard, playerTile)
                    if move == 'quit':
                        endGame = True
                        ex = True
                        self._viewer.buy()
                        continue
                    elif move == 'hints':
                        self._viewer.showHints = not self._viewer.showHints
                        continue
                    elif move == 'fake':  
                        mainBoard.setFake()
                        self._viewer.drawBoard(mainBoard)
                        turn = 'computer'
                        continue
                    else:
                        mainBoard.makeMove(playerTile, move[0], move[1]) 
                    if not mainBoard.getValidMoves(computerTile) == []: 
                        turn = 'computer'
                else:  
                    self._viewer.drawBoard(mainBoard)
                    self._viewer.showPoints(mainBoard, playerTile, computerTile)
                    input('Нажмите Enter чтобы увидеть ход компьютера.') 
                    x, y = self._ai.getComputerMove(mainBoard, computerTile) 
                    mainBoard.makeMove(computerTile, x, y)  
                    if not mainBoard.getValidMoves(playerTile) == []: 
                        turn = 'player'
                if (mainBoard.getValidMoves(playerTile) == []) and (mainBoard.getValidMoves(computerTile) == []):
                    endGame = True  

           
            self._viewer.drawBoard(mainBoard)
            self._viewer.drawFinalResults(mainBoard, playerTile, computerTile)
            if not self._viewer.playAgain():
                ex = True
        self._viewer.buy()