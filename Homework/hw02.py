from asyncio.windows_events import NULL
import base64
from math import prod
from operator import add, mul, sub
#pre-declares
square = lambda x: x * x
identity = lambda x: x
triple = lambda x: 3 * x
increment = lambda x: x + 1

HW_SOURCE_FILE = __file__


#Q1: Product
def product(n, term):

    if n == 1:
        return term(n)
    else:
        return term(n) * product(n - 1, term)



#Q2: Accumulate
def square(x):
    return x * x

def accumulate(combiner, base, n, term):

    if n == 0:
        return term(n) + base
    else:
        return combiner(term(n), accumulate(combiner, base, n - 1, term))

def summation_using_accumulate(n, term):
    return accumulate(add, 0, n, term)

def product_using_accumulate(n, term):
    return accumulate(mul, 0, n, term)


#Q3: Make Repeater
def compose1(func1, func2):
    """Return a function f, such that f(x) = func1(func2(x))."""
    def f(x):
        return func1(func2(x))
    return f


def make_repeater(func, n):

    if n == 0:
        return identity
    elif n == 1:
        return func
    else:
        return compose1(func, make_repeater(func, n - 1))


#Q4: Church numerals
def zero(f):
    '''
    The English number 'zero' essentially refers the time that the function 'f' is applied.
    In zero function, the lambda expression just return the number itself, so no function has been applied.
    '''
    return lambda x: x

def successor(n):
    '''
    Apply the f one more time to a specific number.
    '''
    return lambda f: lambda x: f(n(f)(x))

def one(f):
    '''
    The function f has been applied to x on 1 time.
    '''
    return lambda x: f(x)

def two(f):
    '''
    2 times.
    '''
    return lambda x: f(f(x))

three = successor(two)

def church_to_int(n):
    '''
    As for above English numbers like zero, one and two, they are not really euqal to the numerical meaning of numbers.
    So we have to use one function to convert the abstract 'function applying time' to numerical numbers.
    The increment function can exactly add 1 as it is called.
    Initial number is 0.
    '''
    return n(increment)(0)


def add_church(m, n):
    '''
    (n(increment)(0)): increment has been applied n times. This value is an integral number.
    m(increment)( 'n' ):      then apply it to the numerical number '(n(increment)(0))' 
    '''
    return m(increment)(n(increment)(0))


def mul_church(m, n):

    return m(n(increment))(0)

def pow_church(m, n):
    return n(m)
