

def fibonacci_term(n):
    if n == 1 or n == 2:
        return 1
    return fibo_term(n-1)+fibo_term(n-2)

def fibonacci_term_wo_recursion(n):
    # find term without recursion
    return golden_logic(n)

def golden_logic(n, start1=1, start2=1):
    # naturally starts with fibonacci
    # n is positive integer
    if n <= 0:
        return
    b = start2-start1
    a = start1-b
    for i in range(n):
        term = a+b
        a = b
        b = term
    return term


