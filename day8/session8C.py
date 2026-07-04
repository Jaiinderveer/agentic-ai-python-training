"""
        1. Think of Object
        User: name, phone, email, age, gender, address
        
        2. Create its class (Representation)
        
"""

class User:
    #Constructor function in User
    #self is a ref variable which holds the hashcode of current object
    def __init__(self,name, phone, email, age, gender, address):
        #LHS: creating attributes in object
        #RHS: putting value in attribute
        self.name = name 
        self.phone = phone
        self.email = email
        self.age = age
        self.gender = gender
        self.address = address
        print('[LOG] __init__ | self:',self,type(self))
    #Redefining the constructor removes the old definition of constructor from memory
    # we dont have overloading in python
    def __init__(self, name):
        pass
#3. create real object in memory
# Object Construction Statement
# LHS: user1 is a ref variable which has hashcode of the object
#       It is created in Stack
# RHS: Represents the Object i.e. Container construction in heap
#       empty object, whose hashcode will be returned to the ref variable
user1 = User(name='John',phone='+91 9326778990',email='john@gmail.com',age=20,gender='male',address='redwood shores')
user2 = User(name='Fionna',phone='+91 4526778990',email='fionna@gmail.com',age=25,gender='female',address='country homes')

user3 = user1 # reference copy operation

del user3.address
user1.status = 'online'
# user1 and user3 are two ref vars pointing to the same object
print('user1:',user1,vars(user1))
print('user2:',user2,vars(user2))
print('user3:',user3,vars(user3))