import hashlib

class User:
    
    def __init__(self, name = None, phone = None, email = None,password = None):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = self.encrypt(password)
        
    def input_details(self):
        self.name = input('Enter Your Name: ')
        self.phone = input('Enter Your Phone: ')
        self.email = input('Enter Your Email: ')
        self.password = input('Enter Your Password: ')
    
    def show(self):
        print('~'*20)
        print('User Details')
        print(f'Name: {self.name}')
        print(f'Phone: {self.phone}')
        print(f'Email: {self.email}')
        print('~'*20)
        
    def encrypt(self,data):
        encrypted_data = hashlib.sha256(data.encode()).hexdigest()
        return encrypted_data
    
    def to_csv(self):
        return f'{self.name},{self.phone},{self.email},{self.password}\n'
    
    def to_dictionary(self):
        return vars(self)