f1 = open('program.txt', 'r')
data = f1.read()
sum = 0
for i in data:
    if i == ';':
        sum += 1
print(data)
print(sum)
