#Coding Practice

#Q4: Falling Factorial

def falling(n, k):

    if k == 0:
        return 1
    else: 
        return n * falling(n - 1, k - 1)



#Q5: Sum Digits
def sum_digits(y):


    def curtail(n):
        return (n - n%10) / 10

    if y/10 < 1:
        return y
    else:
        print(y)
        return int(y%10 + sum_digits(curtail(y)))
    


#Q7: Double Eights
def double_eights(n):

    return '88' in str(n)

