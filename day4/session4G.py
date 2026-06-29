# # for outer_index in range(0,5,1):
# for outer_index in range(5):            # O(n)
#     print(outer_index)
#     print('--------------------')
#     for inner_index in range(3):        # O(n^2)
#         print(inner_index,end=' ')
#     print('--------------------')
    
#Chessboard Pattern
# 0 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1 0
# 0 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1 0
# 0 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1 0
# 0 1 0 1 0 1 0 1
# 1 0 1 0 1 0 1 0

white = '\u25A0'
black = '\u25A1'
white_pawn = '\u2659'
black_pawn = '\u265F'
for i in range(8):
    for j in range(8):
        if i == 1:
            print(white_pawn,end=' ')
        elif i == 6:
            print(black_pawn,end=' ')
        elif (i+j)%2 == 0:
            print(white,end=' ')
        else:
            print(black,end=' ')
    print()
    
#task: place every chess piece on board/ finish the chessboard