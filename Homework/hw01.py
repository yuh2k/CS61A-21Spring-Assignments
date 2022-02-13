#1 Syllabus Quiz

#2
from operator import add, sub
def a_plus_abs_b(a, b):

    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

#3
def two_of_three(x, y, z):

    return min(x*x + y*y, y*y + x*x , z*z + y*y)

#4
def largest_factor(n):

    def helper(n, cnt):
        if n % cnt == 0:
            return int(n / cnt)
        else: 
            return helper(n, cnt + 1)
    return helper(n, 2)

#5
def if_function(condition, true_result, false_result):

    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():

    if cond():
        return true_func()
    else:
        return false_func()


def with_if_function():

    return if_function(cond(), true_func(), false_func())


def cond():
    return False

def true_func():
    print('Welcome to')

def false_func():
    print('61A')



#6
def hailstone(n):


    def helper(n, counter):        
        if n == 1:
            return counter
        elif n % 2 == 0:
            return helper(n / 2, counter + 1)
        else:
            return helper(3 * n + 1, counter + 1)

    return helper(n, 1)


