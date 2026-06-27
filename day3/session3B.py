#Indexing
#       0  1  2  3  4  5  6
data = [10,20,30,40,50,10,20]
print(data,id(data),type(data))
print(data[0],data[len(data)-2])

#List supports Duplicates

#set -> works on hashing
# Set does not use Indexing, hence you cannot access a single element
data = {10,20,30,40,50,10,20}
print(data,id(data),type(data))
#Output will be unordered due to hashing
