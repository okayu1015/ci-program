def mult(n,m,a,b):
    c = [[None for j in range(m)] for i in range(m)]
    i = 0
    cnt = 0
    while i < m:
        j = 0
        while j < m:
            d = 0
            k = 0
            while k < n:
                d = d + int(a[i][k]) * int(b[k][j])
                k = k + 1
                cnt += 1
            c[i][j] = d
            j += 1
        i += 1
        
    return c

def matrix(data):
    print(data)
    for n in range(len(data)):
        if data[n] == ',':
            break

    an = int((n+1)/2)
    data = data.replace(',',' ')
    data = data.replace('.','')
    data = data.split()
    print(data)
    am = int(len(data)/an)
    print('行 = ' + str(am))
    print('列 = ' + str(an))
    k = 0
    a = [[None for j in range(an)] for i in range(am)]
    for i in range(0,am):
        for j in range(0,an):
            a[i][j] = data[k]
            k += 1
    return a, am, an

f = open('mat1.txt', 'r')
data = f.read()
f.close()
a, am, an = matrix(data)

print(a)

f = open('mat2.txt', 'r')
data = f.read()
f.close()

b, bm, bn = matrix(data)

print(b)

print(mult(an,am,a,b))
