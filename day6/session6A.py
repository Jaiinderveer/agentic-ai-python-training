# Function in python
# def add_numbers(num1,num2):
# def add_numbers(num1,num2 = 10):
# def add_numbers(num1 =10,num2): #error
def add_numbers(num1 =10,num2 = 20): 
    print('Result is:',num1+num2) 
print(add_numbers,hex(id(add_numbers)),type(add_numbers))

add_numbers(10,20)
add_numbers(num1 = 100,num2=200)
add_numbers(num2 = 110,num1=40)

add_numbers(50)
add_numbers()

#Reference copy operation

add = add_numbers
print(add,hex(id(add)),type(add))
add(100,200)

# You can delete functions also
# del add
# del add_numbers

# add_numbers(10)


