from itertools import count


def log(fun):
    """
    Return a decorator for fun that prints whenever fun is called.
    It should also print the parameter values.
    """
    def wrapper(*args, **kwargs):

        print(args)
        print(kwargs)

        param = ", ".join(tuple(str(param) for param in args) + tuple(f"{key}={kwargs[key]}" for key in list(kwargs.keys())))
        print(f"{fun.__name__}({param})")

        return fun(*args, **kwargs)

    return wrapper
