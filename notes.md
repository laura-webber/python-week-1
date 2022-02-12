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
