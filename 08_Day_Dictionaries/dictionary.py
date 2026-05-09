# syntax
empty_dict = {}
# Dictionary with data values
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

person = {
    'first_name':'Justin',
    'last_name':'Fab',
    'age':23,
    'country':'USA',
    'is_marred':False,
    'skills':['JavaScript', 'Python', 'SQL', 'CSS', 'HTML'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

print(person['first_name'])
person.get("first_name")
person['first_name'] = 'Chris'
person.get('first_name')

person.items()
dct.clear()

dog = {}

dog['name'] = 'Max'
dog['breed'] = 'Shiba Inu'
dog['legs'] = '4'
dog['age'] ='7'

student = {'first_name': 'Justin', 'last_name': 'Fab', 'gender': 'male'}

lst=list(student.keys())

lst