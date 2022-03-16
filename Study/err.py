# def hello_world():
#     def internal():
#         print('Hello world')
#     return internal
#
#
# hello = hello_world()
# print(hello)
# hello()


def print_something(func):
    func()


def say_hello():
    print('Say hello')

print_something(say_hello)
