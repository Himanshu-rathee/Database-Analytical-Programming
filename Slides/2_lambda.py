#%%
#using lambda
x = lambda a,b : a*b
print(x(10,5))

# lambda inside a function
def myfunction(n) :
    return lambda a : a *n

doubler = myfunction(2)
tripler = myfunction(3)
print(f"Multiply by 2 {doubler(5)}")
print(f"Multiply by 3 {tripler(5)}")
