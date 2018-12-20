def g(n):
    g = {}
    g[0] = 1
    for i in range(1,n+1):
        g[i] = (1103515245 * g[i-1] + 12345) % 2**26
    return g[n]

def h(n):
    h = {}
    h[0] = 1
    for i in range(1,n+1):
        h[i] = g(n) % 2**10
    return h[i]

n = k =  0
l = m = 0

flag = 0
num = 100000
min = num
for i in range(1, num):
    for j in range(i+1, num):
        print("(i,j) =" + str(i) + "," + str(j))
        if h(i) == h(j):
            if min > (j-i):
                n = i
                k = j
                
print(n)
print(k)
