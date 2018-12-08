f1 = open('program.txt', 'r')
data = f1.read()
data1 = data.split('\n')

sum = 0
for i in range(len(data1)):
    if data1[0:i].count(data1[i]) != 0:
        print(data1[i])
        sum += 1
print('重複行の総数:' + str(sum))
