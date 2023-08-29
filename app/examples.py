import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

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

def extract_domains(file_name):
    try:
        fhandle = open(file_name)
    except:
        print('Cannot open the file!')
        quit()

    domains = fhandle.read().split()
    print('Domains:', len(domains))
    for domain in domains:
        print(domain.lstrip('.'))

def strip_symbols(text):
    symbols = ['.', ',', '\'', '!', '?']
    stripped_text = ''
    for char in text:
        if char in symbols:
            stripped_text += ' '
            continue
        stripped_text += char
    return stripped_text

def group_duplicates(text_file):
    try:
        fhandle = open(text_file)
    except:
        print('Cannot open the file!')
        quit()

    words = strip_symbols(fhandle.read()).lower().split()

    words_group = {}
    for word in words:
        words_group[word] = words_group.get(word, 0) + 1 

    print(len(words_group), words_group)


def get_most_common_words(file_name, max = 1) :
    # Open the file
    try:
        fhandle = open(file_name, 'r')
    except:
        print('Cannot open the file!')
        quit()

    words = strip_symbols(fhandle.read()).split()

    # Store each word with its iteration count in a dictionary
    words_count = {}
    for word in words :
        words_count[word] = words_count.get(word, 0) + 1
    
    # Loop through the dict and store tuples of (value, key) in a list
    words_list = []
    for key,value in words_count.items() :
        words_list.append((value, key))

    # Sort the list in descending order
    sorted_list = sorted(words_list, reverse=True)

    # Get the first 10 tuples
    # Print the top words
    for count, word in sorted_list[:max] :
        print(word, count)

def extract_domain_names(text) :
    return re.findall('\S+@(\S+)', text)

# print(extract_domain_names('From amr@abc.de.fg Tue Jul 18 06:24 2023 Jack@abc.xyz'))

def extract_spam_rate(text) :
    return re.findall('X-DSPAM-Confidence: ([0-9.]+)', text)
    
# print(extract_spam_rate('X-DSPAM-Confidence: 0.8475'))

def extract_links_from_page(page_url):
    # Open the url
    fhandle = urllib.request.urlopen(page_url)

    # Find all urls using Regex
    urls = {}
    for line in fhandle:
        line = line.decode().strip()
        found_urls = re.findall('"(\S+://\S+)"', line)
        if len(found_urls) > 0:
            # Store the urls
            for url in found_urls:
                urls[url] = urls.get(url, 0) + 1
    return urls

# urls = extract_links_from_page('https://www.yahoo.com')
# for url in urls:
#     print(url)

def bs_example():
    url = 'https://www.yahoo.com'
    data = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(data, 'html.parser')
    
    tags = soup('a')
    for tag in tags:
        print(tag.get('href', None))

bs_example()

