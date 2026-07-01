# Variable Arguments in Python
def add_numbers(*args):
    print(args) # Tuple
    print(type(args))
    print(sum(args))
    
add_numbers(10,20,30,40,50)
add_numbers(10,20,30)
add_numbers(-10,-20,-30)