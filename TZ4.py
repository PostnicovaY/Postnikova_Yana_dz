def type_logger(func):
    def wrapper(*args):
        for arg in args:
            print(f'{arg}: {type(arg)}')
            print(f'{func(arg)}')

    return wrapper

def val_checker(func):
    def wrapper(*args):
        for arg in args:
            try:
                if (arg < 0):
                    raise ValueError(f'wrong val {arg}')
                else:
                    print(f'{arg}: {type(arg)}')
                    print(f'{func(arg)}')
            except Exception as e:
                print(e)

    return wrapper

@val_checker
def calc_cube(*args):
    return [x ** 3 for x in args]

calc_cube(1,2,-7)