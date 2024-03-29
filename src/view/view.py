class View:

    
    def __init__(self):
        self.showHints = False 

    def enterPlayerTile(self):
        
        tile = ''
        while not (tile == 'X' or tile == 'O'):
            print('За кого будешь играть - X или O?')
            tile = input().upper()

        
        if tile == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    def printFirstTurn(self,turn: str):
        print(turn.title() + ' - ходит первым.')

    def drawBoard(self, board, validMoves = None):
       
        if validMoves is None:
            validMoves = []
        HLINE = '  +---+---+---+---+---+---+---+---+'
        print('    1   2   3   4   5   6   7   8')
        print(HLINE)
        for y in range(8):
            print(y + 1, end=' ')
            for x in range(8):
                if [x, y] not in validMoves:
                    print('| %s' % (board.getElement(x, y)), end=' ')
                else:
                    print('| .', end = ' ')
            print('|')
            print(HLINE)

    def showPoints(self, board, playerTile, computerTile):
        
        scores = board.getScoreOfBoard()
        print('У Вас %s очков. У компьютера -  %s очков.' % (scores[playerTile], scores[computerTile]))

    def getPlayerMove(self,board, playerTile):
        
        DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
        while True:
            print('Введите Ваш ход, или введите quit для завершения игры, или hints для включения/выключения подсказки')
            move = input().lower()
            if move == 'quit':
                return 'quit'
            if move == 'hints':
                return 'hints'
            if move == 'fake': 
                return 'fake'

            if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
                x = int(move[0]) - 1
                y = int(move[1]) - 1
                if board.isValidMove(playerTile, x, y) == False:
                    continue
                else:
                    break
            else:
                print('Это неправильный ход. Наберите цифру X (1-8) по горизонтали, и Y (1-8) - по вертикали.')
                print('Например, 81 займет самую правую верхнюю клетку.')

        return [x, y]

    def hi(self):
        print('Реверси приветствует тебя!')

    def buy(self):
        print('Пока, пока!')

    def playAgain(self):
        print('Будем играть еще раз? (yes or no)')
        return input().lower().startswith('y')

    def drawFinalResults(self, board, playerTile, computerTile):
        
        scores = board.getScoreOfBoard()

        print('X набрали %s очков. O набрали %s очков.' % (scores['X'], scores['O']))
        if scores[playerTile] > scores[computerTile]:
            print('Ты обыграл компьютер на %s очков! Я горжусь тобой!!! :)' % (
                        scores[playerTile] - scores[computerTile]))
        elif scores[playerTile] < scores[computerTile]:
            print('Ты проиграл. Компьютер выиграл у тебя %s очков. В следующий раз получится... :(' % (scores[computerTile] - scores[playerTile]))
        else:
            print('НИЧЬЯ!')