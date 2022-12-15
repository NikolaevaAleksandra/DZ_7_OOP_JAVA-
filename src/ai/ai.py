import random

from src.model.model import Board

class Ai:
    # Простой класс для решения, куда сходить на текущем ходе на доске
    def __init__(self):
        pass

    def getComputerMove(self, board, computerTile):
        
        possibleMoves = board.getValidMoves(computerTile)

       
        random.shuffle(possibleMoves)

       
        for x, y in possibleMoves:
            if board.isOnCorner(x, y):
                return [x, y]

       
        bestScore = -1
        for x, y in possibleMoves:
            dupeBoard = Board(board=board.getBoardCopy()) 
                                                          
            dupeBoard.makeMove(computerTile, x, y)              
            score = dupeBoard.getScoreOfBoard()[computerTile]
            if score > bestScore:
                bestMove = [x, y]
                bestScore = score
        return bestMove