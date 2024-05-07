N = int(input("Enter th no of queens:- "))

board = [[0]*N for i in range(N)]
# for i in range(N):
#     temp = []
#     for j in range(N):
#         temp.append(0)
#     board.append(temp)

def isSafe(i,j):
    for p in range(N):
        if board[i][p] == 1 or board[p][j] == 1:
            return False
    
    for n in range(N):
        for m in range(N):
            if i+j == n+m or i-j == n-m :
                if board[n][m] == 1:
                    return False
    
    return True

def nqueen(no_of_queen):
    if no_of_queen == 0:
        return True
    
    for i in range(N):
        for j in range(N):
            if board[i][j] != 1 and isSafe(i,j):
                board[i][j] = 1
                if nqueen(no_of_queen-1) == True :
                    return True  
                board[i][j] = 0 
    return False



def printBoard(board):
    for i in board:
        for j in i:
            print(j, end=" ")
        print()
    
if nqueen(N):
    printBoard(board)
else:
    print("Can't place")