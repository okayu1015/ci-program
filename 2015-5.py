f1 = open('program.txt', 'r')
data = f1.read()
data1 = data.split('\n')
data2 = []

sum = 0
for i in range(len(data1)):
    if data1[0:i].count(data1[i]) == 0 and len(data1[i]) > 20: #2行が完全に一致していない and 20文字以上
        data2.append(data1[i])

for i in range(len(data2)):
    for j in range(0,i):
        nomatch = 0
        
        if len(data2[i]) > len(data2[j]):
            for k in range(len(data2[j])):
                if data2[i][k] != data2[j][k]:
                    nomatch += 1

        if len(data2[i]) <= len(data2[j]):
            for k in range(len(data2[i])):
                if data2[i][k] != data2[j][k]:
                    nomatch += 1
                
        if nomatch < 5:
            print(data2[i])
            print(data2[j])
            sum += 1
        
        

print('類似組の総数:' + str(sum))
