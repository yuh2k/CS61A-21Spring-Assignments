HW_SOURCE_FILE = __file__

# Q1: Num eights
def num_eights(pos):

    def tail(n):
        return int(n%10)
    def rest_of(n):
        return int((n - tail(n)) / 10)
    def isEight(n):
        return n == 8

    def count_helper(cnt, pos):
        if pos == 0:
            return cnt
        else:
            if isEight(tail(pos)):
                return count_helper(cnt + 1, rest_of(pos))
            else:
                return count_helper(cnt, rest_of(pos))
    return count_helper(0, pos) #Start the recursion

# Q2: Ping-pong 
def pingpong(n):
    '''
    n -> n
    cnt: sequence, for limiting
    change_time: the time of changing directions
    value: the value of pingpong
    '''

    def helper(n, cnt, change_time, value):
        if cnt == n:
            return value
        elif change_direction(cnt + 1):
            return helper(n, cnt + 1, change_time + 1, value + pow(-1, change_time))
        else:
            return helper(n, cnt + 1, change_time, value + pow(-1, change_time))

    def change_direction(n):
        return n%8 == 0 or num_eights(n) >= 1

    return helper(n, 1, 0, 1)

# Q3: Missing Digits
def missing_digits(n):

    def tail(n):
        return int(n%10)
    def rest_of(n):
        return int((n - tail(n))/10)
    def make_dif(n):
        return 0 if tail(n) == tail(rest_of(n)) else (tail(n) - tail(rest_of(n)) - 1)
    
    return 0 if n < 10 else make_dif(n) + missing_digits(rest_of(n))

# Q4: Count coins
def get_next_coin(coin):
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def count_coins(change):

    def get(rest, amount):
        if amount is None:
            return 0
        elif rest <= amount:
            return 1 if rest == amount else 0
        else:
            return get(rest - amount, amount) + get(rest, get_next_coin(amount))

    return get(change, 1)


# Q5: Anonymous factorial
from operator import sub, mul

def make_anonymous_factorial():
    """
    I didn't solve this.
    Solution source: https://zhuanlan.zhihu.com/p/160161178
    Try to absorb it
    """
    return (lambda f:lambda x: f(f,x))(lambda f,x:1 if x == 1 else x*f(f,(x - 1)))

print(make_anonymous_factorial()(5))

# Q6: Towers of Hanoi

#2022.02.15 to be solved

