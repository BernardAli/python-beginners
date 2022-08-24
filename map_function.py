# Basic Usage
people = ['Matt', 'Bryan', 'Eddy', 'Mark']

# Old way
counts = []
for x in people:
    counts.append(len(x))
print(counts)

# Modern way
print(f'Mapped: {list(map(len, people))}')

# complex
cars = ['nissan', 'audi', 'volvo', 'tesla']
models = ['x-trail', 'a8', 's60']


def merge(a, b):
    return a + ' ' + b


x = map(merge, cars, models)
print(list(x))


# call multiple in one map call
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def doall(func, num):
    return func(num[0], num[1])


f = (add, subtract, multiply, divide)
v = [[5, 3]]
n = list(v) * len(f)

m = map(doall, f, n)
print(list(m))