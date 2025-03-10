# Příručka na python

### Proměnná
```python
x = 5
y = "Hello, World!"
```

### Datové typy
```python
x = 5           # int
y = 5.5         # float
z = "Hello"     # str
a = True        # bool
```

### Listy
```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list[0])  # Output: 1
```

### Slovníky
```python
my_dict = {"name": "John", "age": 30}
print(my_dict["name"])  # Output: John
```

### Podmínka IF
```python
x = 10
if x > 5:
    print("x is greater than 5")
```

### For ciklus
```python
for i in range(5):
    print(i)
```

### Smyčky While
```python
i = 0
while i < 5:
    print(i)
    i += 1
```

## Funnkce
```python
def my_function():
    print("Hello from a function")

my_function()
```

## Třídy
```python
class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}")

obj = MyClass("John")
obj.greet()  # Output: Hello, John
```

## Import modulů
```python
import math
print(math.sqrt(16))  # Output: 4.0
```

## Manipulace se soubory
```python
with open("file.txt", "r") as file:
    content = file.read()
    print(content)
```

## Zpracování výjimek
```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

## Užitečné vestavěné funkce
```python
len("Hello")  # Output: 5
str(123)      # Output: '123'
int("123")    # Output: 123
```

## Rozšiřování seznamů
```python
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

## Funkce Lambda
```python
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
```

## Mapování, filtrování, redukce
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Map
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# Filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4]

# Reduce
sum = reduce(lambda x, y: x + y, numbers)
print(sum)  # Output: 15