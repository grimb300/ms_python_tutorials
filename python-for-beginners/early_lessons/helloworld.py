first_name = 'Bob'
last_name = 'Grim'
print(first_name + ' ' + last_name)

# String manipulation
sentence = 'This is a sentence'
print(sentence)
print(sentence.capitalize())
print(sentence.upper())
print(sentence.lower())

# String formatting (all should have same output)
output = 'Hello, ' + first_name + ' ' + last_name
print(output)
output = 'Hello, {} {}'.format(first_name, last_name)
print(output)
output = 'Hello, {0} {1}'.format(first_name, last_name)
print(output)
output = f'Hello, {first_name} {last_name}'
print(output)