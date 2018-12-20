import time
import math

start = time.time()

def g(n,phi):
    tmp = phi
    for i in range(n-1):
        tmp = ans(tmp,phi)
    a = ans(tmp,change(1/math.sqrt(5)))
    return a


def change(num):
    num = str("{:.32f}".format(num))
    
    for i in range(32): ##有効数字32桁
        if num[i] == '.':
            break
    num = num.replace('.','')

    return str(num[0:32]) + ' ' + str(i-1)
        
def times(x, y):
    if len(x) <= 2 and len(x) <= 2:
        return int(x) * int(y)
    else:
        a = int(x[0:int(len(x)/2)])
        b = int(x[int(len(x)/2):len(x)])
        c = int(y[0:int(len(y)/2)])
        d = int(y[int(len(y)/2):len(y)])
        sum =  times(str(a),str(c))*(10**int(len(x))) + ((times(str(a),str(c))+times(str(b),str(d)))-((a-b)*(c-d))) * (10**int(len(x)/2)) + times(str(b),str(d))
        return times(str(a),str(c))*(10**int(len(x))) + ((times(str(a),str(c))+times(str(b),str(d)))-((a-b)*(c-d))) * (10**int(len(x)/2)) + times(str(b),str(d))

def ans(x,y):
    x = x.split()
    y = y.split()
    n = 10**(int(x[1])+int(y[1]) - 31*2)
    a = times(x[0],y[0])*n

    return change(a)


phi = (1 + math.sqrt(5)) / 2
phi = change(phi)
print('phi = ' + str(phi))

print('g(140) = ' + str(g(140,phi)))

print('time:' + str(time.time()-start))
