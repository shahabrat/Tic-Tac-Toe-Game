def insertletter(letter,pos):
    board[pos]=letter

def spaceIsFree(pos):
    return board[pos]==' '
def printBoard(board):
    print('  |    |')
    print(' '+board[1]+'| '+board[2]+'  | '+board[3])
    print('  |    |')
    print('---------------')
    print('  |    |')
    print(' ' + board[4] + '| ' + board[5] + '  | ' + board[6])
    print('  |    |')
    print('---------------')
    print('  |    |')
    print(' ' + board[7] + '| ' + board[8] + '  | ' + board[9])
    print('  |    |')

def isWinner(bo,le):
    return (bo[7]==le and bo[8]==le and bo[9]==le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1]==le and bo[4]==le and bo[7]==le) or (bo[2]==le and bo[5]==le and bo[8]==le) or (bo[3]==le and bo[6]==le and bo[9]==le) or (bo[1]==le and bo[5]==le and bo[9]==le) or (bo[3]==le and bo[5]==le and bo[7]==le)

def playermove():
    run=True
    while run:
        move=input('Select a position for X(1-9)')
        try:
            move=int(move)
            if move>0 and move<10:
                if spaceIsFree(move):
                    run=False
                    insertletter('X',move)
                else:
                    print('Sorry!This space is not free.Please select another position')
            else:
                print('Please enter a number in range(1-10)')
        except:
            print('Please enter a number(1-9)')
def computermove():
    possiblemoves=[x for x,letter in enumerate(board) if letter == ' ' and x!=0]
    move=0
    for let in ['O','X']:
        for i in possiblemoves:
            boardcopy=board[:]
            boardcopy[i]=let
            if isWinner(boardcopy,let):
                move=i
                return move

    cornersopen=[]
    for i in possiblemoves:
        if i in [1,3,7,9]:
            cornersopen.append(i)

    if len(cornersopen)>1:
        move=selectrandom(cornersopen)
        return move
    if 5 in possiblemoves:
        move=5
        return move

    edgesopen = []
    for i in possiblemoves:
        if i in [2, 4, 6, 8]:
            edgesopen.append(i)

    if len(edgesopen)>1:
        move=selectrandom(edgesopen)

    return move
def selectrandom(li):
    import random
    ln=len(li)
    r=random.randrange(0,ln)
    return li[r]

def isboardfull(board):
    if board.count(' ') >1:
        return False
    else:
        return True
def main():
    global board
    board = [' ' for x in range(10)]
    print('Welcome to TIC TAC TOE game!')
    printBoard(board)
    while not (isboardfull(board)):
        if not isWinner(board,'O'):
            playermove()
            #printBoard(board)
        else:
            print('Sorry! O\'s win!')
            break
        if not isWinner(board,'X'):
            move=computermove()
            if move == 0:
                print('Tie game')
            else:
                insertletter('O',move)
                print('Computer placed an \'O\' in position: ',move)
                printBoard(board)
        else:
            printBoard(board)
            print('X\'s win!Good Job!')
            break
while True:
    main()
    text=input('Play again?')
    if text.lower() == 'yes':
        continue
    else:
        print('See you soon!')
        break