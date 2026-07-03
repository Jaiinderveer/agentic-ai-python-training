#Product of Elements of a list with Recursion
#Draw the Same in Stack

def product(numbers,length):
    if length == 0:
        return 1
    else:
        previous = product(numbers,length-1)
        current = numbers[length-1]
        return current * previous
    
data = [2,3,8]
result = product(data,len(data))

print('Result is:',result)