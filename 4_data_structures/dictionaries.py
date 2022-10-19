'''
Dictionary: Key-value pairs

- All keys should be unique
e.g cannot have two ages in a dictionary
'''

from unicodedata import name


customer={
    "name":"John Smith",
    'age': 30,
    'is_verified':True
}

# Access items in dictionary
print(customer['name'])

# using the get method
print(customer.get('birthdate')) #None means does not exist
print(customer.get('age'))

# updating
customer['name']='Sarvesh'
print(customer['name'])

#add new key
customer['dob']='14 mar 1999'
print(customer['dob'])