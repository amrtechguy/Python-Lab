# Calculate the work pay
def ex_1():
    # get the hours
    hours = input('Enter your hours: ')
    try:
        hours = float(hours)
    except:
        hours = -1

    # get the rate
    rate = input('Enter your rate: ')
    try:
        rate = float(rate)
    except:
        rate = -1

    # Check if inputs are valid
    if hours == -1:
        print('The hours you entered is not a number!')
    elif rate == -1:
        print('The rate you entered is not a number!')
    # Calculate the pay
    else:
        if hours > 40:
            extra_hours = hours - 40
            pay_for_extra_hours = extra_hours * (1.5 * rate)
            total_pay = pay_for_extra_hours + (40 * rate)  
            print('Your pay is', total_pay)
        else:
            total_pay = pay_for_extra_hours + (hours * rate)  
            print('Your pay is', total_pay)

# Compute Payments
def compute_pay(hours, rate):
    try:
        hours = float(hours)
        rate = float(rate)
    except:
        return 'Invalid hours or rate.'
    
    if hours > 40:
        base_hours = 40
        extra_hours = hours - 40
        base_pay = base_hours * rate
        extra_pay = extra_hours * (rate * 1.5)
        total_pay = base_pay + extra_pay
        return total_pay
    else:
        total_pay = hours * rate
        return total_pay
    
# ex_2
def ex_2():
    hours = input('Enter your hours: ')
    rate = input('Enter your rate: ')
    print(compute_pay(hours, rate))

# get max number
def get_max(nums):
    max_num = nums[0]
    for num in nums:
        if(num > max_num):
            max_num = num
    return max_num

# get total of numbers
def get_total(nums):
    total = 0
    for num in nums:
        total += num
    return total

# get count of array items
def get_count(arr):
    count = 0
    for item in arr:
        count += 1
    return count

# read_numbers
def read_nums():
    nums = []
    while True:
        line = input('> ')
        if line == 'done' :
            total = get_total(nums)
            count = get_count(nums)
            average = total / count
            print('[Results]')
            print('Total:', total)
            print('Count:', count)
            print('Average:', average)
            break
        try:
            num = float(line)        
        except:
            print('Invalid number!')
            continue
        nums.append(num)
    print(nums)

def get_domain_from_text(text = '') :
    start_pos = text.find('@') + 1
    end_pos = text.find(' ', start_pos)
    # pointer = start_pos
    # while text[pointer] != ' ':
    #     pointer += 1
    print(text[start_pos:end_pos])

# get_domain_from_text('From amr@abc.de.fg Mon Jul 17 8:00:01 2023')

def extract_value(text = '') :
    start_pos = text.find(':') + 1
    sliced_str = text[start_pos:]
    stripped_str = sliced_str.strip()
    try:
        value = float(stripped_str)
    except:
        value = stripped_str
    return value

# print(extract_value('X-DSPAM-Confidence: 0.8475 '))

def print_file_content(file_name):
    try:
        fhandle = open(file_name, 'r')
    except:
        print('File cannot be open!')
        quit()

    line_number = 1
    for line in fhandle:
        print(line_number, line.rstrip().upper())
        line_number += 1


print_file_content('poem.txt')