def sumple_func(x,l=[]):
    l.append(x)
    return l

y=[1,2,3]
r=sumple_func(100,y)
print(r)
r=sumple_func(200,y)
print(r)