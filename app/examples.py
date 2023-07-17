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

# Working space
ex_1()