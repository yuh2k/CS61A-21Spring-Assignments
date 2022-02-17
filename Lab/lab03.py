
HW_SOURCE_FILE = __file__

# Q3: Summation
def summation(n, term):

    assert n >= 1
    return term(1) if n == 1 else term(n) + summation(n - 1, term)

  
# Q4: Pascal's Triangle

# Solution 1: Recursion
def pascal(row, column):
    '''
    Pascal's Triangle AKA Yanghui's Triangle:
    
   col|
    0 |            1
                 (0,0)

    1 |        1        1
             (1,0)    (1,1)
           
    2 |     1       2       1
          (2,0)   (2,1)   (2,2)
          
    3 |  1      3       3       1
       (3,0)  (3,1)   (3,2)   (3,3)
    
    In this triangle, each number equals the sum of numbers that on its two shoulders.
    '''
    if column == 0:
        return 1
    elif column <= row:
        return pascal(row - 1, column - 1) + pascal(row - 1, column)
    else:
        return 0


# Q4: Pascal's Triangle

#Solution 2: Factoriaal
def pascal(row, column):
    '''
                       (row - col)! * col!
    C(row, col) =     --------------------
                              row!
                             
    '''

    fact = lambda n: 1 if n == 1 else n * (fact(n - 1))
    pos =  lambda row, column: fact(row) / (fact(row - column) * fact(column))
    return 1 if row == 0 else int(pos(row, column))
        
        
# Q5: Repeated, repeated
def compose1(f, g):
    """"Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h


def repeated(f, n):
    return lambda x: x if n == 0 else compose1(f, repeated(f, n - 1))(x)

