"""
    DSA -> 3 questions a day
    design patterns -> https://refactoring.guru/design-patterns
    solid principles -> https://www.designgurus.io/answers/detail/solid-design-principles
    forward deployed engineer
    
"""

# Vehicle: registration_no., fasttag_id, type
# FastTag: fasttag_id, bank, balance

# 1 Vehicle has 1 FastTag
class FastTag:
    
    def __init__(self,fasttag_id, bank, balance):
        self.bank = bank
        self.fasttag_id = fasttag_id
        self.balance = balance
    def show(self):
        print('~~~~~~~~~~~~~~FAST TAG~~~~~~~~~~~~~~')
        print(f'{self.fasttag_id} | {self.bank} | {self.balance}') #Formatted string
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
class Vehicle:
    
    def __init__(self,registration_no, fasttag, type):
        self.registration_no = registration_no
        self.fasttag = fasttag
        self.type = type

    def show(self):
        print('~~~~~~~~~~~~~~VEHICLE~~~~~~~~~~~~~~')
        print(f'{self.registration_no} | {self.type}')
        print('{registration_no} | {type}'.format_map(vars(self)))
        
        self.fasttag.show()
        
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        print('~'*30 + '\n')