data = [10,20,30,40,50]
# data = {10,20,30,40,50}
# print(data[0])
# print(data[1])
# print(data[2])
# print(data[3])
# print(data[4])

# Loop -> Iterate

# #For Each/ Enhanced For Loop
# # Read Only Loop
# for number in data:
#     print(number)
    
# # Start from 0 and go till $ i.e. less than 5
# for index in range(0,5)
# for index in range(0,len(data))
# for index in range(len(data))
# for index in range(0,len(data),2):
    # print(data[index])
    
for index in range(len(data)):
    data[index] = data[index]*2
    
print(data)

# While Loop -> traditional loop
idx = 0
while(idx<5):
    print(data[idx])
    idx+=1