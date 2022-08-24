def outline(func):
    def inner(*args, **kwargs):
        print('-' * 20)
        print(f'Function: {func.__name__}')
        func(*args, **kwargs)
        print('-' * 20)

    return inner


@outline
def test(a, b):
    try:
        assert(a > 0)
        assert(b > 0)
    except AssertionError:
        # specific
        print(f'Failed to assert a:{a} and b:{b}')
    except TypeError:
        print(f'Wrong type a:{a} and b:{b}')
    except Exception as e:
        print(f'Something bad happened, {a}, {b} {e}')
    else:
        z = a / b
        print(f'Result: {z}')
    finally:
        print('Done')


test(2, 0)
test(2, 'cat')
test(2, 5)


class CatError(RuntimeError):
    def __init__(self, *args):
        self.args = args


@outline
def test_cats(qty):
    try:
        if not isinstance(qty, int):
            raise TypeError("Must be an int")
        if qty < 9:
            raise CatError("Must own more than 9 cats")
    except Exception as e:
        print(f'Oops: {e.args}')
    finally:
        print('Complete')

test_cats(2)
test_cats(12.3)
test_cats(2)
test_cats('abc')

    
