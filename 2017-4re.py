def search(a):
    i = 0
    j = 0
    ans = ''
    mv = 1
    while j < len(data[0]):
        if a[i][j:j+4] == '****':
            if a[i+2][j:j+4] == '   *':
                ans += '7'
                j += (4+mv)
            else:
                if a[i+4][j:j+4] == '   *':
                    ans += '9'
                    j += (4+mv)
                else:
                    if a[i+2][j:j+4] == '*  *':
                        ans += '0'
                        j += (4+mv)
                    else:
                        if a[i+1][j] == '|':
                            if a[i+1][j+3] == '|':
                                ans += '8'
                                j += (4+mv)
                            else:
                                ans += '5'
                                j += (4+mv)
                        else:
                            if a[i+3][j] == '|':
                                ans += '2'
                                j += (4+mv)
                            else:
                                ans += '3'
                                j += (4+mv)
        elif a[i][j] == ' ':
            for k in range(len(a)-1):
                if a[k][j] == '*':
                    break
            if k != (len(a)-2):
                i = k
            else:
                j += 1

        else:
            if a[i][j:j+4] == '*  *' and a[i+2][j:j+4] == '****':
                ans += '4'
                j += (4+mv)
            elif a[i][j:j+4] == '*' and a[i+3][j] == '|':
                ans += '6'
                j += (4+mv)
            else:
                ans += '1'
                j += (1+mv)
    return ans


f = open('out2.txt', 'r')
data = f.read()
print(data)
data = data.split('\n')
print(len(data)-1)
print(search(data))


f.close()
