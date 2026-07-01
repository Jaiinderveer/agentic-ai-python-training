#Debugging

#function -> piece of code which contains logic(Controller) that can be used repeatedly
#   logic which needs to be reused

# max = data[0];
# for index in range(1,len(data)):
#     if data[index]> max:
#         max = data[index]
# print('Max in Data is:',max)
        
# max = scores[0];
# for index in range(1,len(scores)):
#     if scores[index]> max:
#         max =scores[index]
# print('Max in scores is:',max)
        
# max = prices[0];
# for index in range(1,len(prices)):
#     if prices[index]>max:
#         max = prices[index]
# print('Max in prices is:',max)
        
data = [10,20,50,70,30,15]
scores = [27,110,35,89,20,30]
prices = [1500,3000,5000,1200,4500]
def find_max(numbers):
    max = numbers[0]
    for index in range(1,len(numbers)):
        if numbers[index] > max:
            max = numbers[index]
    print('Max in', numbers,'is:',max)
    
find_max(numbers = data)
find_max(numbers = scores)
find_max(numbers = prices)