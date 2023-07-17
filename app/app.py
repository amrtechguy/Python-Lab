# Data Types
def data_types():
    print((31)) # int
    print(type(31.6)) # float
    print(type('Amr')) # str

# Type Casting
def type_casting():
    print(type(int('123'))) # casting str to int
    print(type(str(123))) # Casting an integer to a string
    print(type(float(100))) # Casting int to float
    print(int(99.50)) # The fraction is removed when casting float to int

# On division output is always float
def operators():
    print('# On division output is always float')
    print('8/2 =',8/2)

# Error handling try/except
def error_handling():
    age = input('Enter your age: ')

    try:
        age = int(age)
        print('Your age is', age)
    except:
        print('You did not enter a anumber!')

# Conditionals
def conditionals():
    user_id = input('Enter your ID: ')

    try:
        user_id = int(user_id)
    except:
        user_id = -1
    
    if user_id == '31':
        print('Welcome to the club. (^_^)')
    elif user_id == str(33):
        print('Welcome to the club. (^_^)')
    else:
        print('Sorry, your ID is not acceptable!')

# Exit the program
# exit() === quit()
def exit_program():
    print('Hi, I\'m Amr!')
    exit()
    print('I\'m a tech guy.')
