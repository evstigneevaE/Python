def validate_args(func):
    def wrapper(*args):
        if len(args) < 1:
            return "Not enough arguments"
        elif len(args) > 1:
            return "Too many arguments"
        elif not isinstance(args[0], int):
            return "Wrong types"
        elif args[0] < 0:
            return "Negative argument"
        else:
            return func(*args)
    return wrapper

@validate_args
def example_function(x):
    return x

print(example_function(5))  # Output: 5
print(example_function())  # Output: Not enough arguments
print(example_function(5, 10))  # Output: Too many arguments
print(example_function("5"))  # Output: Wrong types
print(example_function(-5))  # Output: Negative argument

