def square_of_number(number):
    print('>> [square_of_number] start')
    
    my_numbers = []
    
    for index in range(len(number)):
        my_numbers.append(number[index]) 
    print('>> [square_of_number] Before:',my_numbers,id(my_numbers))
    for index in range(len(my_numbers)):
        my_numbers[index] = my_numbers[index] ** 2
    
    print('>> [square_of_number] After:',my_numbers,id(my_numbers))
    print('>> [square_of_number] end')
    
def main():
    print('>> [Main] start')
    data = [10,20,30,40,50]
    print('>> [Main] Before:',data,id(data))
    square_of_number(data)
    print('>> [Main] After:',data,id(data))
    print('>> [Main] End')
    
if __name__ == '__main__':
    main()