print(f'Name: {__name__}')
print(f'File: {__file__}')


def test():
    print('This is a test function')


def main():
    print('This is the main function')
    test()


# Run automatically
if __name__ == "__main__":
    main()