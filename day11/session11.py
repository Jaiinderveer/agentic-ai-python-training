file = open('day10/Session10C.py','r')
# file = open('C:/Users/jaiin/Downloads/awesome.txt','r')
# print(type(file))

# data = file.read()
# print(type(data))
# print(len(data))
# print(data)

# lines = file.readlines()
# file.close() # release memory resources
# print(type(lines))
# print(len(lines))

# for line in lines:
#     print(line)
    
with open('day10/Session12C.py') as file:
    lines = file.readlines()
    for line in lines:
        print(lines)
file.close()
print('program finished')