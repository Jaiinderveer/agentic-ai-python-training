"""
    Strings in Python
"""

# cafe_name = 'Johns Cafe'
# cafe_name = "John's Cafe"
# cafe_name = """Johns Cafe
# Redwood Shores
# +91 9316009876
# """

cafe_name = 'John\'s Cafe'
print(cafe_name)

# Strings are IMMUTABLE
# they cannot be changed
# Whenever u manipulate the string, you get a new string in memory
names = 'john, jennie, jim, jack, joe'
upper_case_names = names.upper()
print('names:',names , type(names), id(names))
print('upper_case_names:',upper_case_names,type(upper_case_names),id(upper_case_names))

names_split = names.split(', ')
print('names_split:',names_split,type(names_split),id(names_split))

order = 'i want to order chai samosa with pakora'

keywords = order.split(' ')
print(keywords)

if 'chai' in keywords:
    print('What kind of Tea you want?')
    
# email = input('Enter Your Email: ')
# password = input('Enter Your Password: ')
# print('Email Entered',email)
# print('Password Entered',password) #Regular Expression (regex)

# if '@' in email and '.' in email and len(password)>8:
#     print('Valid Email and Valid Password')
# else:
#     print('Invalid Email or Password')

vehicle_no = 'PB10GX3307'
#indexing
print(vehicle_no[0])
print(vehicle_no[-1])

# Negative Indexing
print(vehicle_no[-1])
print(vehicle_no[-2])

#slicing
print(vehicle_no[0:2])
print(vehicle_no[2:4])
print(vehicle_no[4:])
print(vehicle_no[:5])

# Pythonic way to use slicing to reverse a string
print(vehicle_no[::-1])

# String Concatenation
full_name = 'John' + ' ' + 'Watson'
print(f'Full Name is: {full_name}')

line = '='*60

print(line)

# password = '          password123        '.strip()
# password = '          password123        '.rstrip()
password = '          password123        '.lstrip()
bill_amt = '23.45000'.rstrip('0')

print(password)
print(bill_amt)