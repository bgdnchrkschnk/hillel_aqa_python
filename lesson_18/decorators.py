from datetime import datetime

def my_decorator(func):
    def wrapper():
        print("Do smthing before function...")
        func()
        print("Do smthing after function...")
    return wrapper

# def decorator_before(func):
#     def wrapper():
#         print(datetime.now())
#         print("Do something before function..")
#         func()
#     return wrapper
#
# def decorator_after(func):
#     def wrapper():
#         func()
#         print("Do something after function..")
#         print(datetime.now())
#     return wrapper

def my_decorator_with_params(func):
    def wrapper(*args, **kwargs):
        print("Do smthing before function...")
        func(*args, **kwargs)
        print("Do smthing after function...")
    return wrapper

def my_decorator_with_params_return(func):
    def wrapper(*args, **kwargs):
        print("Do smthing before function...")
        result = func(*args, **kwargs)
        print("Do smthing after function...")
        return result
    return wrapper

if __name__ == '__main__':

    # @decorator_after # post condition
    # @decorator_before # pre condition
    @my_decorator
    def func() -> None:
        print("Some functionality")

    @my_decorator_with_params
    def func_repeat(repeat: int = 1) -> None:
        print("Some functionality"*repeat)

    # @my_decorator_with_params_return
    # def func_repeat_return(repeat: int = 1) -> str:
    #     res = "Some functionality" * repeat
    #     return res
    #
    #
    # func_repeat_return()
