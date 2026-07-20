import re

text = 'Python is easy to learn'

# if 'easy' in text #membership testing

result = re.search('easy',text)

print('result:',result)

if result:
    print('easy searched and found')
else:
    print('Cannot find easy')
    
text = 'Order id 101 costs 2500 inr'

result = re.findall(r"\d+",text)
print('result:',result)

text = """
this is awesome
john@example.com
we are learning regular expressions in python
admin@finlo.in
hello@gmail.com
"""
result = re.findall(r"\S+@\S+.",text)
print('result:',result)

phone = '9316009876' # exactly 10 digit phone number
result = re.fullmatch(r"\d{10}",phone)
print('result:',result)

pan = 'BBVPK2144K'
result = re.fullmatch(r"[A-Z]{5}[0-9]{4}[A-Z]",pan)
if result:
    print('PAN is OK!')

vehicle_number = 'PB10GX3307'
result = re.fullmatch(r"[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}",vehicle_number)
if result:
    print('Vehicle Number is OK!')
    
text = """i want to place a call to +919876512345 and send an email to john@example.com
as my vehicle PB10GX3307 is having a flat tyre, i need help immediately"""

Phone,Email,Vehicle = re.findall(r"\+[0-9]{12}|[a-z]+@[a-z]+\.[a-z]+|[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}",text)
print('Phone:',Phone)
print('Email:',Email)
print('Vehicle Number:',Vehicle)