def g(n):
    g = {}
    g[0] = 1
    for i in range(1,n+1):
        g[i] = (1103515245 * g[i-1] + 12345) % 2**26
    return g[n]

n = k = m = 0
flag = 0
num = 1000000000
min = num
gg = 1
for i in range(1, num):
    gg = (1103515245 * gg + 12345) % 2**26
    if 1 == gg:
        print(i)
