def square_of_number(number):
    print('>> [square_of_number] start')
    print('>> [square_of_number] Before:',number,id(number))
    number *= number
    print('>> [square_of_number] After:',number,id(number))
    print('>> [square_of_number] end')
    
def main():
    print('>> [Main] start')
    data = 10
    print('>> [Main] Before:',data,id(data))
    square_of_number(data)
    print('>> [Main] After:',data,id(data))
    print('>> [Main] End')
    
if __name__ == '__main__':
    main()