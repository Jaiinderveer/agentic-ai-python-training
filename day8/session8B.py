"""
        1. Think of Object
        User: name, phone, email, age, gender, address
        
        2. Create its class (Representation)
        
"""

class User:
    #Constructor function in User
    #self is a ref variable which holds the hashcode of current object
    def __init__(self):
        print('[LOG] __init__ | self:',self,type(self))

#3. create real object in memory
# Object Construction Statement
# LHS: user1 is a ref variable which has hashcode of the object
#       It is created in Stack
# RHS: Represents the Object i.e. Container construction in heap
#       empty object, whose hashcode will be returned to the ref variable
user1 = User()
user2 = User()
user3 = user1 # reference copy operation
# user1 and user3 are two ref vars pointing to the same object
user1.name = 'John'
user2.full_name = 'fionna flynn'
user3.age = 20
user2.age = 25
user3.email = 'jai@gmail.com'
print(user1,vars(user1))
print(user2,vars(user2))
print(user3,vars(user3))