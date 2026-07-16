import datetime
user_input = 'create task: create 3 licenses for finlo, Create licenses on immediate basis for Jujhar Group for bus ticketing, call, Gourav, 9915571177'
data1 = user_input.split(':')
print(data1)

data2 = data1[1].split(', ')
print(data2)

task = {
    'title': data2[0].strip(),
    'description': data2[1].strip(),
    'action': data2[2].strip(),
    'contact_name': data2[3].strip(),
    'contact_phone': data2[4].strip(),
    'status': 'PENDING',
    'created_at': datetime.datetime.now()
}

print(task)