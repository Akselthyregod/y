import numpy as np
import sympy as sp

x = sp.Symbol('x')
e = np.e
n = sp.cos(2*x*np.pi)

def printAns(func, input):
    print(f'{input} => {func.subs(x,input)}')

def getAns(func, input):
    return func.subs(x,input)

f = -20*e**-(x**2/8) - e**(1/2 * n) + 20 + e
f_prime = f.diff(x)
f_prime2 = f_prime.diff(x)


#print(f'f(0) = {f.subs(x,0)}')
#print(f'f(x) = {f}')
#print(f'f\'(x) = {f_prime}')
#print(f'f\'\'(x) = {f_prime2}')

#printAns(f_prime,3)

def play(func_prime, guess):
    
    x = getAns(func_prime, guess)
    count = 0

    step = 0.0000001
  


    while(abs(getAns(func_prime, x)) > 0.0001 and count < 100):
        
        x = x - getAns(func_prime, x)*step

        count = count + 1
       ## step = 1 / getAns(f_prime2, x)
        
    print(step)
    print(count)

    return x

print(play(f_prime, 10))


def printFunc():

    for i in range(10):
        print(f' {i}: {f_prime.subs(x,i)}')

