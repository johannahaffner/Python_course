
def absolute(x): 
    if x >= 0:
        return ('The absolute value of x is', x)
    else:
        return ('The absolute value of x is', x*(-1))

def maximum(a):
    y = a[0]
    for i in a:
        if i > y:
            y = i
    return y

def dot_product(v,w): 
    s = 0
    if len(v) == len(w):
        for i in v:
            for j in w:
                s = s + i*j
        return s
    else:
        print('Matrix dimensions not compatible')

def average(b):
    h = 0.0
    count = 0
    for i in b:
        h = h + i 
        count = count + 1
    c = h/count
    return c

x = -79
t = absolute(x)
print(t)

li = [1, 2, 3, -4, 5, 0, -9, 10, 1, 19, 3, 0]
z = maximum(li)
print('The maximum value in li is', z)

l = [7, -9, 3, 4, 7, 1, -6, 0]
m = [1, 3, -7, 15, 1, 1, 1, 1]
r = dot_product(l,m)
print('The dot product of l and m is', r)

n = [13, -44, 72, 3, 0, 7, 0, 1]
q = average(n)
print ('The average value in n is', q)
