
class Person:
    # weak private
    _name = "No name"

    def setName(self, name):
        self._name = name
        print(f'Name set to {self._name}')

    # strong private
    def __think(self):
        print('Thinking to myself')

    def work(self):
        self.__think()

    # Before and After
    def __init__(self):
        print('Constructor')

    def __call__(self, *args, **kwargs):
        print('call someone')


class Child(Person):
    def testDouble(self):
        self.__think(self)
