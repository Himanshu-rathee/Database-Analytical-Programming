# function which can have additional parameters i.e.  *args
def arbitarary(x, y, *more):
    print("x = ",x," y = ",y)
    print("arbitrary: " , more)
    for i in more:
        print("arbitrary also in *more: ", i)

arbitarary(10,20,30,60,50)

# function which can have additional parameters i.e.  **kargs

def keyargs(x, y, **kwargs) :
    print("X = ",x)
    print("Y = ", y)
    for key,values in kwargs.items():
        print(key, " : ", values)

keyargs(10, 20, first ='Sobil', last='Dalal')