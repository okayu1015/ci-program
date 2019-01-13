import queue
def calculate(m, n, a, b):
    c = [[[]for i in range(m)] for i in range(m)]
    i = 0
    cnt = 0
    while i < m:
        j = 0
        while j < m:
            d = 0
            k = 0
            while k < n:
                d = d + int(a[i*n+k]) * int(b[k*m+j])
                k += 1
                cnt += 1
            c[i][j] = d
            j += 1
        i += 1
    return c


f = open('mat1.txt', 'r')
a = f.read()
cnt = 0
for i in range(len(a)):
    if a[i] == ',':
        cnt += 1
a = a.replace(',', ' ')
a = a.replace('.', ' ')
a = a.split()
print(a)
print(cnt+1)
print(int(len(a)/(cnt+1)))

f = open('mat2.txt', 'r')
b = f.read()
b = b.replace(',', ' ')
b = b.replace('.', ' ')
b = b.split()
print(b)

print(calculate(cnt+1,int(len(a)/(cnt+1)), a, b))
