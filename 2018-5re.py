def calculate(m, n, s):
    c = [[[]for i in range(m)] for i in range(m)]
    q = []
    a = []
    b = []

    cnt = 0
    q_cnt = 0
    for i in range(m*n):
        a.append(str(i))
    for i in range(m*n):
        b.append(str(i + m*n))

    i = 0
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


print(calculate(3,4,24))
