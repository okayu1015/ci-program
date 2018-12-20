import math

a = float((1 + math.sqrt(5)) / 2)

def change(ans):
    print('ans = ' + str(ans)) ##通常表記
    ans = str("{:.32f}".format(ans))
    
    for i in range(32): ##有効数字32桁
        if ans[i] == '.':
            break
    ans = ans.replace('.','')

    return str(ans[0:32]) + ' ' + str(i-1)

print(change(a))
