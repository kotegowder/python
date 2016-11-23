board = [[],[],[],[],[]]

for i in range(0,5):
    for j in range(0,5):
        board[i].append('O')

def print_board(board):
    for row in board:
        print " ".join(row)
    
print_board(board)
