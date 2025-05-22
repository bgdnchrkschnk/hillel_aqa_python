
def decorator_repeater(repeat_times: int = 1):
    def outer(func):
        def wrapper(*args, **kwargs):
            for num in range(repeat_times):
                func(*args, **kwargs)
        return wrapper
    return outer

def decorator_split(func):
    def wrapper():
        result = func()
        return result.split()
    return wrapper

def decorator_x3(func):
    def wrapper():
        for num in range(3):
            func()
    return wrapper

@decorator_split
def return_string() -> str:
    return 'Hello World!'

# @decorator_x3
@decorator_repeater(repeat_times=5)
def say_hello() -> None:
    print("Hello World!")

@decorator_repeater(repeat_times=2)
def say_hello_name(name: str) -> None:
    print(f"Hello World! My name is {name}")

say_hello_name("Olha")

