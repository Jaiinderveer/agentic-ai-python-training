# Conditional Operators -> will always return True or False
# >, <, >=, <=, ==, !=

# Membership Operators
# is, in , not in, is not


# Logical Operators
# and, or, not
# wallet_amt = 300
# cab_fare = 300

# print('can i book the cab?',(wallet_amt>=cab_fare))

# boolean
# internet = True

# print(cab_fare is wallet_amt)
# print(cab_fare is not wallet_amt)
# print(cab_fare == wallet_amt)
# print(cab_fare != wallet_amt)

# Assignment -> == vs is and is not vs !=

# numbers = [10,20,30]
# print(10 in numbers)
# print(100 not in numbers)

# internet = True
# gps = False

# print('Can i Navigate?', (internet and gps))

email = 'admin@example.com'
password = 'admin123'

user_email = input('Enter Email to Login: ')
user_pswd = input('Enter password to Login: ')

print('Login Success?',(user_email == email and user_pswd == password))