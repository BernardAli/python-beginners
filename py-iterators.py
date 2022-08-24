# Iterators
# Making Counting easy


# Iter Basics
# Lists, tuple, dict, set
# They are iterable containers yout can get an iterators from


people = ['Ben', 'Isaac', 'Muna']
i = iter(people)
print(i)
print(next(i))
print(next(i))
print(next(i))
# print(next(i)) # Stop Iteration


# Iterable class
import random


class Lotto:
    def __init__(self):
        self.max =  5

    def __iter__(self):
        for _ in range(self._max):
            yield random.randrange(1, 90)
    
    def setMax(self, value):
        self._max = value

print('-'*30)


lotto = Lotto()
lotto.setMax(5)

for x in lotto:
    print(x)

print('-'*30)