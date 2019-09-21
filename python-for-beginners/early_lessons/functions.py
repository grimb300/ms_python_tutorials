from datetime import datetime

# Print the current time (parameter to use a task name)
def print_time(task_name):
  print(task_name)
  print(datetime.now())
  print()

first_name = 'Susan'
print_time('first name assigned')

for x in range(0, 10):
  print(x)
print_time('range printed')

# Can create default values for the parameters
def get_initial(name, force_uppercase=True):
  if force_uppercase:
    initial = name[0:1].upper()
  else:
    initial = name[0:1]
  return initial

first_name = input('Enter your first name ')
first_name_initial = get_initial(first_name)

print('Your initial is ' + first_name_initial)