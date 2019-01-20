def search(a):
    i = 0
    j = 0
    ans = ''
    mv = 2
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

        else:
            if a[i][j:j+4] == '*  *' and a[i+2][j:j+4] == '****':
                ans += '4'
                j += (4+mv)
            elif a[i][j:j+4] == '*   ':
                ans += '6'
                j += (4+mv)
            else:
                ans += '1'
                j += (1+mv)
    return ans


f = open('out1.txt', 'r')
data = f.read()
print(data)
data = data.split('\n')
print(data[0][0:3])
print(search(data))


f.close()
