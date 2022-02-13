print('20 days are ' + str(50) + ' minutes')
print(20 * 24 * 60)
print(f'20 days are {50} minutes')
print(f'20 days are {20 * 24 * 60} minutes')

to_seconds = 20 * 24 * 60
print(f'20 days are {to_seconds} minutes')

name_of_unit = 'seconds'

print(f'20 days are {to_seconds} {name_of_unit}')


def days_to_units(num_of_days):
    print(f'Function output: {num_of_days} days are {to_seconds} {name_of_unit}')


days_to_units(20)


def days_to_units_message(num_of_days, message):
    if num_of_days > 0:
        print(f'Function with message output: {num_of_days} days are {to_seconds} {name_of_unit}, {message}')
    else:
        return "you entered a negative value"


days_to_units_message(20, 'hi there')

greeting = input('hi Laura, enter a greeting\n')
print(greeting)
