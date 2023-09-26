art_galleries= {'11234':{}}
galleries_11234= [('A', '763'), ('D', '375'), ('P', '377')]
# convert the list of tuple into a dictionary value
# art_galleries['11234'].update(galleries_11234)
art_galleries['11234'] = galleries_11234
print(type(art_galleries['11234'])) # a dictionary {'A':'763', 'D':'375'...}
# if using assignment, it is still a list of tuple

# print(art_galleries['11234'].items()) # return a list of tuples [('A, '763')...]
mydict = {}
mydict.update([('A', '123'), ('B', '345')])
mydict.update([('A', '321')])
print(mydict)

# Create a nested dictionary
data = {
    'person': {
        'name': 'John',
        'age': 30,
        'address': {
            'street': '123 Main St',
            'city': 'Anytown',
            'zipcode': '12345'
        }
    }
}

# To access the 'name' key within the nested dictionary:
name = data['person']['name']
print(name)  # Output: 'John'

# To change the value of 'age':
data['person']['age'] = 31

# To access the 'city' key within the 'address' dictionary:
city = data['person']['address']['city']
print(city)  # Output: 'Anytown'

# To assign a new value to 'city':
data['person']['address']['city'] = 'Newtown'
