"""
    assignment: Another brick in the wall
    
    customer - 13 bricks -> can be any number
    iteration 1  -> 3
    john 1 
    jack 2
    iteration 2 -> 3+6 = 9
    john 2
    jack 4
    iteration 3 -> 9 + 3 + 1 = 13
    john 3
    jack 6 -> 1
    
    answer: Who placed the last brick and how many
    jack placed the last brick , qty: 1
    
"""

# CONTROLLER
# for/if/else/operators

number_of_bricks = int(input('Enter Number of Bricks: '))

remaining = number_of_bricks
n = 1     

while remaining > 0:
        bricks = min(n, remaining)
        remaining -= bricks
        
        if remaining == 0:
            print("John placed the last brick, qty:", bricks)
            break
        
        bricks = min(2 * n, remaining)
        remaining -= bricks
        
        if remaining == 0:
            print("Jack placed the last brick, qty:", bricks)
            break
        n += 1

