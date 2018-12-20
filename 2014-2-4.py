import time

def f(x):
    y = 0
    z = 0
    for i in range(1,x+1):
        if i <= 2:
            tmp = 1
            y = 1
            z = 1
        else:
            tmp = y + z
            z = y
            y = tmp
    return tmp

             

    
start = time.time()
print('f = ' + str(f(50)))

print(time.time()-start)
