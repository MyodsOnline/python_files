


def deco(func):
    print(f'Decorated function - {func.__name__}')
    func()
    return func

@deco
def inner():
    print("I'm inner func")
