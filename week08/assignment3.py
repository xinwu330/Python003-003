def partial1(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = {**keywords, **fkeywords}
        return func(*args, *fargs, **newkeywords)
    # newfunc.func = func
    # # newfunc.args = args
    # newfunc.keywords = keywords
    return newfunc

def multiply(x,y):
        return x * y

# create a new function that multiplies by 2
dbl = partial1(multiply,2)
print(dbl(8))