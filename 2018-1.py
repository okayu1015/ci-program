def argo(n,m):
    i = 0
    cnt = 0
    while i < m:
        j = 0
        while j < m:
            d = 0
            k = 0
            while k < n:
                d = d + 1
                k = k + 1
                cnt += 1
            c = d
            j += 1
        i += 1
        
    return cnt

print(argo(3,4))
print(argo(5,6))
#答えはn*m*m回？
