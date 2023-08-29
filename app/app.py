import re
import socket
import urllib.request, urllib.parse, urllib.error
import sqlite3

# Data Types
def data_types():
    print(type(31)) # int
    print(type(31.6)) # float
    print(type('Amr')) # str
    print(type(True)) # bool
    print(type(None)) # NoneType

# Chars Ordinary
def char_ord():
    print(ord('A')) # Returns the decimal number of a given char

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

# Data structure: List
def ds_list():
    value = None # Has no length
    random_data = [33, 'Amr Hassan', 10.00, ['SWE', 'CS']] # Lists can store different data types

    text = 'version = 1.0'
    # text[0] = 'V' # str is immutable -> cannot be changed
    # print(text)

    nums = [1, 200, 33, -5, 0]
    # nums[0] = 100
    # print(nums)

    # print(len(text), len(nums))

    range_nums = range(5, 10, 2)
    # for num in range_nums:
    #     print(num)

    # rand_nums = list() # Create an empty list
    # rand_nums = [33, 15, 0, 1]
    # rand_nums.append(70)
    # rand_nums.insert(1, 5)
    # rand_nums.extend([1, 2, 3]) # add a list at the end
    # rand_nums.remove(5)
    # rand_nums.reverse()
    # rand_nums.sort()
    # print(rand_nums)

    config_rule = 'safe-mode = true'
    # print(config_rule.split('=').pop().strip())

    email_header = 'From amr@abc.de.fg Tue Jul 18 06:24 2023'
    print(email_header.split()[1].split('@')[1])

# Data structure: Dictionary / Hashmap / Associative Array
def ds_dictionary():
    user = dict()
    user['name'] = 'Amr Hassan'
    user['country'] = 'Egypt'
    
    configs = {'ver': '1.0', 'safe_mode': False}

    persons = {101: 'Amr Hassan', 880: 'Someomne'}

    print(persons.get(101))
    print(persons.keys())
    print(persons.values())
    print(persons.items()) # [{key: value}, {key: value}]

    for key,value in persons.items(): # .items() -> a list of tuples
        print(key, value)

# Data structure: Tuple
def ds_tuple():
    tpl = (100, 2, 200) # Is immutable -> Cannot be changed 
    
    roles = ('Software Engineer', 'Manager', 'Office boy', 'Manager')
    # print(roles.count('Manager'))
    # print(roles.index('Manager'))

    a, b, c, d = ['a', 'b', 'c', 'd'] # a list assigned to variables
    e, f, g, h = roles # a tuple assigned to variables

    ('amr', 'peter') > ('adam', 'sally') # false -> compare element by element / letter by letter until reaching a difference
   
    print(sorted({'role': 'SWE', 'name': 'Amr Hassan'}.items())) 

# Regex
def regex() :
    # text = 'This is my resume'
    # print(text.find('my'))
    # print(re.search('my', text))
    # print(text.startswith('my'))
    # print(re.search('^my', text))
    
    # ^     starts with
    # .     match any chars
    # \S    Non-whitespace chars
    # \s    whitespace chars
    # *     0 or more of the preceding expression
    # +     1 or more of the preceding expression
    # ?     don't be greedy
    # ()    extraction boundries -> extract only what matches inside the ()
    # []    to match a set of characters
    # [^ ]  don't match what's after ^ -> whitespace in this example
    # \     escape a character

    fhandle = open('config.ini', 'r')
    for line in fhandle :
        # print(re.search('^X.*:', line.rstrip()))
        # print(re.search('^X-.*:', line.rstrip()))
        # print(re.search('^a.*b', line.rstrip()))
        # print(re.search('^a+b', line.rstrip()))
        # print(re.search('^a.+b', line.rstrip()))
        # print(re.findall('[0-9]+', line.rstrip()))
        # print(re.findall('^X-.+?:', line.rstrip()))
        # print(re.findall('\S+@\S+', line.rstrip()))
        # print(re.findall('^From (\S+@\S+)', line.rstrip()))
        return

def sockets() :
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('dr-chuck.com', 80))
    cmd = 'GET http://dr-chuck.com HTTP/1.0\n\n'.encode()
    mysock.send(cmd)
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode())
    mysock.close()

def my_urllib():
    fhandle = urllib.request.urlopen('https://data.pr4e.org/romeo.txt')
    for line in fhandle:
        print(line.decode().strip())

class Person:

    name = ''
    job = ''

    def __init__(self, data):
        print('A new user is created.')
        self.name = data['name']
        self.job = data['job']
    
    def __del__(self):
        print('The user is deleted.')

class User(Person):
    id = 0

# new_user = User({'name': 'Amr Hassan', 'job': 'Security Engineer'})
# print(new_user.name, new_user.job)

def add_user_to_db(name, email):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # Create the user's table if not exist
    cursor.execute('CREATE TABLE IF NOT EXISTs `user` (`id` INT NOT NULL UNIQUE, `name` TEXT NOT NULL, `email` TEXT NOT NULL, PRIMARY KEY(`id` AUTOINCREMENT))')

    # Check email duplication
    cursor.execute('SELECT `id` FROM `user` WHERE `email` = ?', (email,))
    record = cursor.fetchone()
    if record is None:
        cursor.execute('INSERT INTO `user` (`name`, `email`) VALUES(?, ?)', (name, email))

    connection.commit()
    cursor.close()

def register_user():
    # Ask for user's info
    name = input('Enter the user\'s name: ')
    email = input('Enter the user\'s email: ').lower()

    if len(name) < 1 or not re.search('[a-z0-9]+@[a-z0-9]+[.a-z0-9]+', email):
        print('Invalid name or email.')
    else:
        add_user_to_db(name, email)
    
register_user()