"""
    data = [10,20,30]
    data: [10]
    if len(data) == 1:  
        max -> data[0]
        
    data: [10,20]
    if len(data) == 1:  
        max -> data[0]
    else:
        if data[0]>data[1]:
            return data[0]
        else:
            return data[1]
"""

# def get_max(numbers,length):
#     if length == 1:
#         return numbers[0]
#     else:
#         if numbers[length-2]>numbers[length-1]:
#             return get_max(numbers,length-1)
#         else:
#             numbers[length-2] = numbers[length-1]
#             return get_max(numbers,length-1)
def get_max(numbers,length):
    if length == 1:
        return numbers[0]
    else:
        previous = get_max(numbers,length-1)
        curr = numbers[length-1]
        if previous<curr:
            return curr;
        else:
            return previous


data = [10,40,50,20]
result = get_max(data,len(data))
print('Max is:',result,data)