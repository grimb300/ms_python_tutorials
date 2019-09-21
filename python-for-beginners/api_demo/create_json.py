import json

# Create a dictionary object
person_dict = {'first': 'Bob', 'last': 'Grim'}
# Add additional key pairs to dictionary as needed
person_dict['city'] = 'Portland'

# Create a list of programming languages
languages_list = ['JavaScript', 'Python', 'php']
person_dict['languages'] = languages_list

# Create a staff dictionary
staff_dict = {}
staff_dict['program manager'] = person_dict

# Convert dictionary to JSON object
person_json = json.dumps(person_dict)
staff_json = json.dumps(staff_dict)

# Print JSON object
print(person_json)
print(staff_json)