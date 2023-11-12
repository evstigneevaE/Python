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

def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper

import time

def timer(func):    
    def wrapper(*args, **kwargs):
        start_time = time.time()          
        result = func(*args, **kwargs)    
        end_time = time.time()            
        execution_time = end_time - start_time  
        print(f"Время выполнения функции {func.__name__}: {execution_time:.20f} секунд")
        return result                   
    return wrapper

@validate_args
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


fib_without_memoize = timer(fibonacci)
print('Фибоначчи без memoize с аргументом 35: ', fib_without_memoize(35))

fibonacci = memoize(fibonacci) 
fib_with_memoize = timer(fibonacci)     
print('Фибоначчи с memoize и аргументом 35: ', fib_with_memoize(35))  







