# Search Operation: Linear Search O(n)
data = [10,20,30,40,50]
number_to_search = int(input('Enter a Number to Search: '))

# def search(numbers,number_to_search):
    
#     for number in numbers:
#         print('[LOG] Comparing:',number,'with',number_to_search)
#         if number == number_to_search:
#             print('Number Found:',number)
#             break
#     else:
#         print('Number Not Found')

# search(data,number_to_search)

def search(*numbers,**number_to_search):
    
    for number in numbers:
        print('[LOG] Comparing:',number,'with',number_to_search['a'])
        if number == number_to_search['a']:
            print('Number Found:',number)
            break
    else:
        print('Number Not Found')

search(10,20,30,40,50, a = number_to_search)