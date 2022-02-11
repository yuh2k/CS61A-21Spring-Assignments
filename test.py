import sys
sys.setrecursionlimit(10000)

def largest_factor(n):
    """Return the largest factor of n that is smaller than n.
    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    def multi_to_exp(fac, expect):
        product = 1
        if product == expect:
            return fac

        elif expect % fac == 0:
            product *= fac 
            # print(fac)
            return multi_to_exp(fac + 1, expect)
        elif product != expect:
            return multi_to_exp(fac + 1, expect)

    return multi_to_exp(1, n)

res = largest_factor(10)
print(res)