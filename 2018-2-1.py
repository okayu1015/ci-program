#moji = input()
moji = 'SSSSj0013ssTb0010f'
#moji = 'TSSSSb0012fssTTj0006'
#moji = 'j0018j0013Tfj0011j0006'

s = 0
t = 0
i = 0
while i <= len(moji):
    if moji[i] == 'S':
        s += 1
        i += 1
    if moji[i] == 's':
        s -= 1
        i += 1
    if moji[i] == 'T':
        t += 1
        i += 1
    if moji[i] == 't':
        t -= 1
        i += 1
    if moji[i] == 'f':
        print("1")
        break
    if moji[i] == 'j':
        i = int(str(moji[i+1]) + str(moji[i+2]) + str(moji[i+3]) + str(moji[i+4])) - 1 
    if moji[i] == 'b':
        if s > 0:
            i = int(str(moji[i+1]) + str(moji[i+2]) + str(moji[i+3]) + str(moji[i+4])) - 1
        else:
            i += 5

print('(s,t) = (' + str(s) + ',' + str(t) + ')')
            
