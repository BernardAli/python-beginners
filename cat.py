class Cat:
    name = ''
    age = 0
    color = ''

    def __init__(self, name, age=0, color='white'):
        self.color = color
        self.name = name
        self.age = age
        print(f"Constructor for {self.name}")

    def meow(self):
        print(f'{self.name} meow')

    def sleep(self):
        print(f'{self.name} zzz')

    def hungry(self):
        for x in range(5):
            self.meow()

    def sleep(self):
        print(f'{self.name} nom nom nom')

    def description(self):
        print(f'{self.name} is {self.age} year old  {self.color} cat')

