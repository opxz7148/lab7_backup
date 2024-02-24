"""Your code for Exercise 1 of Lab 7."""
from typing import Callable

def randgen(a, b) -> Callable:
    """Returns a new function that takes no parameters,
       and returns random integers between a and b, inclusive.
    """
    return 0


def sum_fun(num_calls: int, fun) -> Callable:
    """Returns a new function that calls the function (fun) `num_calls` times
       and returns the sum of the return values from `fun`.

       :param num_calls: non-negative number of times to call fun. May be 0.
       :param fun: a function that takes no arguments and returns a number
       :returns: a new function that returns sum of calls to fun
    """
    return lambda : 0


def test_sum_fun():
    """A test of the sum_fun function.  Run this using pytest."""
    # TODO replace this code with a very long sequence of ints
    values = [1, 2, 3, 4]
    test_fun = None # function to return next value from values
    roll = sum_fun(0, test_fun)
    # should always be zero
    assert roll() == 0
    assert roll() == 0
    # verify that sum_fun did not call test_fun
    assert 1 == test_fun()
    # test sum of multiple calls
    roll = sum_fun(3, test_fun)
    assert roll() == 2+3+4
    assert roll() == 5+6+7
    roll = sum_fun(5, test_fun)
    assert roll() == 8+9+10+11+12

def test_sum_fun2():
    """Use a built-in function from itertools module instead of
       writing your own test_fun.
    """
    counter = None # TODO
    # test sum of multiple calls
    roll = sum_fun(4, counter)
    assert roll() == 1+2+3+4
    assert roll() == 5+6+7+8
    roll = sum_fun(6, counter)
    assert roll() == 9+10+11+12+13+14


def compose(f, g):
    """Returns a new function that is the the composition of f and g,
       that means:   
       h = compose(f, g)
       h(x) is f(g(x))
       >>> f = lambda x: x*x
       >>> g = lambda x: x+1
       >>> h = compose(f, g)
       >>> h(4)
       25
       >>> h(1)
       4
     """
     return 0
