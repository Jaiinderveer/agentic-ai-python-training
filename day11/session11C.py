# Python Built In Module (JSON)
import json

order={
    'oid':1,
    'customer':'john',
    'dishes':'dal, paneer, roti',
    'amount':500
}

# print(type(order))
# print(order)

# Dictionary to JSON (String representation of dictionary)
json_order = json.dumps(order)
print(json_order)
print(type(json_order))

# JSON to Dictionary (String converted to dictionary)
order_dictionary = json.loads(json_order)
print(order_dictionary)
print(type(order_dictionary))
