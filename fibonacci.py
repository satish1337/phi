

def fibo_term(n):
    if n == 1 or n == 2:
        return 1
    return fibo_term(n-1)+fibo_term(n-2)

def fibo_term_wo_recursion(n):
    # find term without recursion
    if n <= 2:
        return 1
    a = 1
    b = 1
    term = 0
    for i in range(3, n+1):
        term = a+b
        a = b
        b = term
    return term
