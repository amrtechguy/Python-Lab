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

# get_max
def get_max(nums):
    max_num = nums[0]
    for num in nums:
        if(num > max_num):
            max_num = num
    return max_num

# Working space
print(get_max([-10, -2, -3, -4, -5]))