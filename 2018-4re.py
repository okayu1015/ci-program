s = 10
def calculate(m, n, a, b):
    c = [[[]for i in range(m)] for i in range(m)]
    q = []
    i = 0
    cnt = 0
    q_cnt = 0
    while i < m:
        j = 0
        while j < m:
            d = 0
            k = 0
            while k < n:
                d = d + int(a[i*n+k]) * int(b[k*m+j])
                a1 =  int(a[i*n+k])
                b1 =  int(b[k*m+j])
                if a1 in q:
                    q.remove(a1)
                    q.append(a1)
                elif len(q) == s and a1 not in q:
                    q.pop(0)
                    q.append(a1)
                    q_cnt += 1
                elif len(q) < s and a1 not in q:
                    q.append(a1)
                    q_cnt += 1      
                if b1 in q:
                    q.remove(b1)
                    q.append(b1)
                elif len(q) == s and b1 not in q:
                    q.pop(0)
                    q.append(b1)
                    q_cnt += 1
                elif len(q) < s and b1 not in q:
                    q.append(b1)
                    q_cnt += 1      

                print('q過程:' + str(q))
                k += 1
                cnt += 1
            c[i][j] = d
            j += 1
        i += 1
    print('q:' + str(q))
    print('読み出し回数:' + str(q_cnt))
    print('cnt:' + str(cnt))
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

f = open('mat1-2.txt', 'r')
b = f.read()
b = b.replace(',', ' ')
b = b.replace('.', ' ')
b = b.split()
print(b)

print(calculate(cnt+1,int(len(a)/(cnt+1)), a, b))
