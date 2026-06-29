white = '\u25A0'
black = '\u25A1'
white_pawn = '\u2659'
black_pawn = '\u265F'
white_rook = '\u2656'
black_rook = '\u265C'
white_knight = '\u2658'
black_knight = '\u265E'
white_bishop = '\u2657'
black_bishop = '\u265D'
white_king = '\u2654'
black_king = '\u265A'
white_queen = '\u2655'
black_queen = '\u265B'
black_pieces = [
    black_rook, black_knight, black_bishop,
    black_queen, black_king,
    black_bishop, black_knight, black_rook
]

white_pieces = [
    white_rook, white_knight, white_bishop,
    white_queen, white_king,
    white_bishop, white_knight, white_rook
]
for i in range(8):
    for j in range(8):
        if i == 0:
            print(black_pieces[j], end=' ')
        elif i == 1:
            print(black_pawn,end=' ')
        elif i == 6:
            print(white_pawn,end=' ')
        elif i == 7:
            print(white_pieces[j], end=' ')
        elif (i+j)%2 == 0:
            print(black,end=' ')
        else:
            print(white,end=' ')
    print()