# Data Types
def data_types():
    print(type(31)) # int
    print(type(31.6)) # float
    print(type('Amr')) # str
    print(type(True)) # bool
    print(type(None)) # NoneType

# Type Casting
def type_casting():
    print(type(int('123'))) # casting str to int
    print(type(str(123))) # Casting an integer to a string
    print(type(float(100))) # Casting int to float
    print(int(99.50)) # The fraction is removed when casting float to int

# Operators
# def operators():
#     print('a' == 'A')
#     print(1 == 1.0)
#     print('a' is 'A') # Means identical to. (1 is 1.0 -> False)
#     print('a' is not 'A') # Means not identical to. (1 is not 1.0 -> True)
#     print(8/2) # Division results float

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
# exit() == quit()
def exit_program():
    print('Hi, I\'m Amr!')
    exit()
    print('I\'m a tech guy.')

# Infinite Loop
def while_loop():
    while True:
        command = input('> ')
        if(command == 'exit'):
            print('Goodbye!')
            break
        elif(command == 'help'):
            print('This is Help Page.exit')
        else:
            print('This command is not recognized!')

# Definite loop
def for_loop():
    for num in [1, 2, 3, 4, 5] :
        print('Number:', num)
    print('Done!')

# Strings
def strings():
    line = 'Hello,' # str is an array of characters
    line += ' Amr!' # Added value must be type str
    print(line[0]) # Access the char at index 0
    print(line[-1]) # Access a char from the end
    print(line[0:5]) # Slice a string from index 0 up to index 5 (5 is not included)
    print(line[:])
    print(line[:5])
    print(line[7:])
    print(len(line)) # len() -> returns the length of a string
    print('Amr' in line) # Using in as a logical operator
    print(line.lower())
    # print(dir(line)) # Display supported methods for the string class
    print(type(u'عمرو'))

# Files Handling
def files_handling():
    fhandle = open('poem.txt', 'r')
    line_number = 1
    for line in fhandle:
        if line.startswith('And'):
            print(line_number, line.rstrip())
        line_number += 1

# Testing Area
files_handling()