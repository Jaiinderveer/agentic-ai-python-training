#Single value container
a = 10
b = a #Reference Copy Operation | Deep Copy
#Multi value Container
data = [10,20,30,40,50]
numbers = data #Reference Copy Operation | Shallow Copy
phone_wp = ['Hi','Hello',30,40,50]
laptop_wp = phone_wp

numbers[2] = 1000

print("a:",a,id(a))
print("b:",b,id(b))

print("data: ", data,id(data))
print("numbers: ", numbers,id(numbers))

phone_wp[2] = 'Hello Yash'
print("phone_wp: ", phone_wp,id(phone_wp))
print("laptop_wp: ", laptop_wp,id(laptop_wp))

b = 100

print("a:",a,id(a))
print("b:",b,id(b))

#task: identify the use cases where u see reference copy in real life