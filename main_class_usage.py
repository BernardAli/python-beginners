from cat import Cat


def test():
    b = Cat('Defender', 1, 'black')
    b.description()
    b.meow


if __name__ == '__main__':
    x = Cat('test')
    print(x)
    test()