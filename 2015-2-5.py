def g(n):
    g = {}
    g[0] = 1
    for i in range(1,n+1):
        g[i] = (1103515245 * g[i-1] + 12345) % 2**26
    return g[n]
print(g(1))
print("g(2) = " + str(g(2)))
print("g(3) = " + str(g(3)))
