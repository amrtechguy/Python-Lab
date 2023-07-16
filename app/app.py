# Data Types
print('# Data Types')
print('type of 31:', type(31)) # int
print('type of 31.6:', type(31.6)) # float
print('type of \"Amr\":', type('Amr')) # str
print('\n')

# Type Casting
print('# Type Casting')
print('type(int(\"123\")) =',type(int('123'))) # casting str to int
print('type(float(100)) =',type(float(100))) # Casting int to float
print('int(99.50) =',int(99.50)) # The fraction is removed when casting float to int
print('\n')

# On division output is always float
print('# On division output is always float')
print('8/2 =',8/2)
print('\n')

# Receive input from console
print('# Receive input from console')
old_in_years = input('How old are you?') # Data is received as str
print('So, you\'re', old_in_years, 'years old.') # Comma adds a space
print('\n')