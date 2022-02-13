Output
- `print()`

Data Types
- String - anything between single or double quotes
- Int
- Float
- Boolean

String Concatenation
- plus sign (+)
- explicit conversion to string

```python
print('20 days are ' + str(50) + ' minutes')
```

clean, easier version with templating:

```python
print(f'20 days are {50} minutes')
```

'f' stands for 'format'. Only Python3 versions support this feature

Variables

Just name the variable and use assignment operator. No data type declaration.
Naming convention: snake case rather than camel case.

Reserved words

Can't use for variable names

Variable interpolation

```python
print(f'20 days are {to_seconds} minutes')
print(f'20 days are {to_seconds} {name_of_unit}')
```

Functions

define by the `def` keyword

```python
def days_to_units():
    print(f'20 days are {to_seconds} {name_of_unit}')
```

- calling the function
`days_to_units()
`
- with a parameter

```python
def days_to_units(num_of_days):
    print(f'Function output: {num_of_days} days are {to_seconds} {name_of_unit}')
```

With 2 parameters

```python
def days_to_units_message(num_of_days, message):
    print(f'Function with message output: {num_of_days} days are {to_seconds} {name_of_unit}, {message}')
```

Scope
- global variable - variables available from within any scope
- local variable - variables created within a function and only available there

User Input
`input()`
- Built-in function to ask user for input
- Input with prompt

`input('hi Laura, enter a greeting\n')`

Functions with return values

```python
def days_to_units_message(num_of_days, message):
    return f'Function with message output: {num_of_days} days are {to_seconds} {name_of_unit}, {message}'
```

`input()` always treated as a string, so won't do math correctly automatically

- casting `int(user_input)`

```python
user_input = input('enter a number of days you want to use for the formula')
user_input_number = int(user_input)

days_to_units(user_input_number)
```

Conditionals
- use for input validation
```python
def days_to_units_message(num_of_days, message):
    if num_of_days > 0:
        print(f'Function with message output: {num_of_days} days are {to_seconds} {name_of_unit}, {message}')
    else:
        return 'you entered a negative value'
```

Booleans
- `True` or `False` (capitalized)
```python
def the_function():
    if int(user_input) > 0:
        return 'something'
    elif int(user_input) < 0:
        return 'someting else'
    else:
        return 'nothing'
```
- check if something is a number:
`if user_input.isdigit():`

Nested if/else

Try/Except
```python
def validate_and_execute():
    user_input = input("please enter a number: ")
    try:
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = user_input_number * 2
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0. please enter a valid number")
        else:
            print("you entered a negative number. no bueno")
    except:
        print("your input is not a valid number")
```
While Loop

```python
user_input = ""
while user_input != "exit":
     user_input = input("please enter a comma separated list of numbers: ")
     for num_of_days in user_input.split(", "):
         validate_and_execute(user_input)
```

Lists (Arrays)

```python
my_list = ['January', 'February', 'March']
print(my_list)
print(my_list.append('April'))
print(my_list)
print(my_list[3])
```

Comments
- done with # sign in Python for one line
- multiline comments:
  - """ at beginning and end """

Set
- basically a list but with no duplicates
- elements in sets are immutable - can only add or delete elements
- `set()` function can turn a list into a set
```python
num_list = [20, 30, 40, 20, 50, 30]
set_list = set(num_list)
print(set_list)
```
output
`{40, 50, 20, 30}`