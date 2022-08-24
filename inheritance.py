class Feline:
    def __init__(self, name):
        self.name = name
        print('Creating a feline')

    def meow(self):
        print(f'{self.name} meow')

    def sleep(self):
        print(f'{self.name} zzz')

    def setName(self, name):
        print(f'{self} setting name: {name}')
        self.name = name


class Lion(Feline):
    def roar(self):
        print(f'{self.name}  roar')


class Tiger(Feline):
    def __init__(self, name):
        self.name = name
        # super().__init__('No Name')
        print('Creating a tiger')
    
    def stalk(self):
        print(self.name)

    
    def rename(self, name):
        super().setName(name)

c = Feline('kitty')
print(c)
c.meow()

l = Lion('Leo')
print(l)
l.meow()
l.roar()

t = Tiger("Ben")
print(t)
t.stalk()
t.rename("Eddie")
t.stalk()