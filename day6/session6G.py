# for index in range(1,6,1):
#     print(index)

def print_number(number):
    if number>10:
        return
    print(number)
    print_number(number+1) #Execute the same function again from itself
    
print_number(1)