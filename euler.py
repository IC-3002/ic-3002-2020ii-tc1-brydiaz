def e_cuadratica(n):
    # Implemente esta función
    i=0
    e=0
    while(i!=n):
        e=e+1/factorial(i)
        i+=1
    return e


def e_lineal(n):
    # Implemente esta función
    i=0
    factorial=1
    e=0
    while(i!=n):
        e=e+1/factorial
        i+=1
        factorial=factorial*i
    return e


def factorial(num):
    factorial=1
    while(num>0):
        factorial=factorial*num
        num=num-1
    return factorial 
