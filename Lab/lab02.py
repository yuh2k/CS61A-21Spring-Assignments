# Q3: Lambdas and Currying
def lambda_curry2(func):
    return lambda x: lambda y : func(x, y)

def count_cond(condition):
    def cond(N):
        i = 0
        cnt = 0
        for i in range(1, N + 1):
            if condition(N, i):
                cnt += 1
        return cnt   
    return cond

  
# Q7: Composite Identity Function
def compose1(f, g):
    return lambda x: f(g(x))

def composite_identity(f, g): 
    def judge(x):
        return compose1(f, g)(x) == compose1(g, f)(x)
    return judge

# Q8: I Heard You Liked Functions...
def cycle(f1, f2, f3):
  
    def cycle_operater(n):
      
        def help(x):
            if n == 0:
                return x
            else:
                if n % 3 == 1:
                    return f1(cycle_operater(n - 1)(x))
                elif n % 3 == 2:
                    return f2(cycle_operater(n - 1)(x))
                else:
                    return f3(cycle_operater(n - 1)(x))
        return help
    return cycle_operater
        
