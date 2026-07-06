"""
    OOPS
    Object is Model, We need to think about data associated with object

    User: name, phone, email

"""

class User:

    """
    def __init__(self, name=None, phone=None, email=None):
        self.name = name
        self.phone = phone
        self.email = email
    """

    """
    def __init__(self, 
                 name=input('Enter Name: '), 
                 phone=input('Enter Phone: '), 
                 email=input('Enter Email: ')):
        self.name = name
        self.phone = phone
        self.email = email
    """
    """
    def __init__(self):
        self.name = input('Enter Name: ')
        self.phone = input('Enter Phone: ')
        self.email = input('Enter Email: ')
        print('[User] [init] User Object Constructed', self)
    """
    
    def __init__(self, name=None, phone=None, email=None):
        self.name = name
        self.phone = phone
        self.email = email
        print('[User] [init] User Object Constructed', self)

    def input_user_details(self):
        self.name = input('Enter Name: ')
        self.phone = input('Enter Phone: ')
        self.email = input('Enter Email: ')

    def show_user_details(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~')
        print(self.name, self.phone, self.email)
        print('~~~~~~~~~~~~~~~~~~~~~~~')

# user1 = User()
# user1.input_user_details()
# user1.show_user_details()
# print(vars(user1))


print(User)
print(vars(User))