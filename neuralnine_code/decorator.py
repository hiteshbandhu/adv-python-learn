def decorator(function):

    def wrapper(*args, **kwargs):
        print("Decorated")
        function(*args, **kwargs)

    ## note ## as the function is in the wrapper scope, you cannot pass arguments and then get the output, you'd have to pass them through wrapper function.

    return wrapper


@decorator
def hello(name: str):
    print(f"Hello {name}")


hello("hitesh")


# an example of how you can use decorators for logging

from datetime import datetime

now = datetime.now()


def logged(function):
    def wrapper(*args, **kwargs):
        fname = function.__name__
        value = function(*args, **kwargs)
        with open("./logfile.txt", "+a") as f:
            f.write(f"{now} : The Function {fname} returned value {value}\n\n")
            f.close()
        print(f"Function {fname} returned value {value}")
        return value

    return wrapper


@logged
def add(x, y):
    return x + y


print(add(4, 8))
