f = open('mat1.txt', 'r')
d = f.read()
print(d)
cnt = 0
for i in range(len(d)):
    if d[i] == ',':
        cnt += 1
d = d.replace(',', ' ')
d = d.replace('.', ' ')
d = d.split()
print(d)
print(cnt+1)
print(int(len(d)/(cnt+1)))
