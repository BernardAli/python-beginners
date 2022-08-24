# skipping

for _ in range(5):
    print('Hello')


# Test class
from person import *

# Before (single)
# Internal use only, a weak private
p = Person()
p.setName("Ben")
print(f'Weak private {p._name}')


# Before (Double)
# Internal use only, avoid conflict in subclass
p = Person()
p.work()
# p.__think()


c = Child()
# c.testDouble()
c.work()


# After (Any)
class_ = Person()
class_.work()


# Before and After
d = Person()
d.__call__()