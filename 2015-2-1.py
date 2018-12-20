def f(n):
    f = {}
    f[0] = 1
    for i in range(1, n+1):
        if n < 1:
          f[i] = 1
        else:
            f[i] = (161 * f[i-1] + 2457) % 2**24
    return f[n]

print('f(100) = ' + str(f(100)))
