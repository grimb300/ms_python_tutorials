# This code won't run at all
# x = 42
# y = 0
# if x == y
#   print('Success!')

# This code will fail when run
# x = 42
# y = 0
# print(x / y)

# The right way to handle exceptions
x = 42
y = 0
z = 7

print('Expecting an exception')
try:
  print(x / y)
except ZeroDivisionError as e:
  print('Sorry, something went wrong')
else:
  print('Something really went wrong')
finally:
  print('This always runs')

try:
  print(x / y)
except ZeroDivisionError as e:
  # Optionally, log e somewhere
  print('Sorry, something went wrong')
except:
  print('Something really went wrong')
finally:
  print('This always runs on success or failure')
print('This one should succeed')
try:
  print(x / z)
except ZeroDivisionError as e:
  # Optionally, log e somewhere
  print('Sorry, something went wrong')
except:
  print('Something really went wrong')
finally:
  print('This always runs on success or failure')