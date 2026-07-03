
def sort(data):
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            print('i:',i,'j:',j)
            if(data[j]>data[j+1]):
                data[j],data[j+1] = data[j+1],data[j]
numbers = [10,30,20,5,15]
sort(numbers)
print('numbers:',numbers)