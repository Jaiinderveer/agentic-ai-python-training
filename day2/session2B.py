# yash_physics = 70
# yash_chemistry = 80
# yash_maths = 85

# jai_physics = 75
# jai_chemistry = 90
# jai_maths = 95

# yash_marks = [70,80,85]
# jai_marks = [75,90,95]

# List of List
# class_marks = [
#     [70,80,85],
#     [75,90,95]
# ]
#              0  1  2  3  4  5
# yash_marks = [70,80,85,'B','A','A']
# print(yash_marks,id(yash_marks),type(yash_marks))
# print(len(yash_marks))
# print(yash_marks[0],id(yash_marks[0]),type(yash_marks[0]))
# print(yash_marks[1],id(yash_marks[1]),type(yash_marks[1]))
# print(yash_marks[2],id(yash_marks[2]),type(yash_marks[2]))
# print(yash_marks[3],id(yash_marks[3]),type(yash_marks[3]))
# print(yash_marks[4],id(yash_marks[4]),type(yash_marks[4]))
# print(yash_marks[5],id(yash_marks[5]),type(yash_marks[5]))

# yash_marks[1] = 'B'
# print(yash_marks[1],id(yash_marks[1]),type(yash_marks[1]))

#            0  1  2
# yash_marks = 70,80,85
# print('Yash_marks: ',yash_marks,id(yash_marks),type(yash_marks))
# yash_marks[0] = 75
#Tuple is immutable -> You Cannot modify the content | READ ONLY
#list is mutable -> You can modify the content

#activity-> how does list of list stored in memory(stack and heap)

class_marks = [
    [70,80,85],
    [75,90,95]
]

print(class_marks,id(class_marks),type(class_marks))

print(len(class_marks))

print(class_marks[0],id(class_marks[0]),type(class_marks[0]))
print(class_marks[1],id(class_marks[1]),type(class_marks[1]))

print(len(class_marks[0]))
print(len(class_marks[1]))

print(class_marks[0][0],id(class_marks[0][0]),type(class_marks[0][0]))
print(class_marks[0][1],id(class_marks[0][1]),type(class_marks[0][1]))
print(class_marks[0][2],id(class_marks[0][2]),type(class_marks[0][2]))
print(class_marks[1][0],id(class_marks[1][0]),type(class_marks[1][0]))
print(class_marks[1][1],id(class_marks[1][1]),type(class_marks[1][1]))
print(class_marks[1][2],id(class_marks[1][2]),type(class_marks[1][2]))