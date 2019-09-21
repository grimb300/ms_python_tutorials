# Operations
first_num = 6
second_num = 2
print(first_num + second_num)  # = 8
print(first_num * second_num)  # = 12
print(first_num ** second_num) # = 36 ('**' is exponent)

# String concatenation
days_in_feb = 28
# Python doesn't like this because '+' can be number or string operation
# print(days_in_feb + ' days in February')
# Instead need to convert number to string
print(str(days_in_feb) + ' days in February')

# Storing a number as a string
str_first_num = input('Enter the first number ')
str_second_num = input('Enter the second number ')
# Returns concatenated strings
print(str_first_num + str_second_num)
# Convert to number
print(int(str_first_num) + int(str_second_num))
print(float(str_first_num) + float(str_second_num))