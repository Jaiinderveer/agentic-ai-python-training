def add_numbers(num1 =10,num2 = 20): 
    print('Result is:',num1+num2) 

print(add_numbers,hex(id(add_numbers)),type(add_numbers))

#Redefination of Function
# Old definition deleted and new definition created

add = add_numbers

def add_numbers(num1 = 10,num2=20,num3=30):
    print('Result is:',num1+num2+num3)
    
print(add_numbers,hex(id(add_numbers)),type(add_numbers))

add_numbers()

add()