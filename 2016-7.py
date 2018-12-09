data = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9,"ten":10,
        "eleven":11, "twelve":12, "thirty":13, "fourteen":14, "fifteen":15,
        "sixteen":16, "seventeen":17, "eighteen":18, "nineteen":19,}
data1 = {"twenty":20, "thirty":30, "fourty":40, "fifty":50,
        "sixty":60, "seventy":70, "eighty":80, "ninety":90}
data2 = {"hundred":100, "thousand":1000}

def change_eng(num):
    sum = 0
    i = 0
    while i < len(num):

        if num[i] in data:
            if i+1 < len(num):
                if num[i+1] in data2:
                    sum += data[str(num[i])] * data2[str(num[i+1])]
                    i += 2
            else:
                sum += data[str(num[i])]
                i += 1
                    
        elif num[i] in data1:
            if i+1 < len(num) and num[i+1] in data:
                
                if i+2 < len(num) and num[i+2] in data2:
                    sum += (data1[str(num[i])] + data[str(num[i+1])]) * data2[str(num[i+2])]
                    i += 3
                else:
                    sum += (data1[str(num[i])] + data[str(num[i+1])])
                    i += 2
            else:
                sum += data1[str(num[i])]
                i += 1
                    
        elif num[i] in data2:
            sum += data2[str(num[i])]
            i += 1
            
    return sum

#y = 'fifty four thousand three hundred twelve'
y = input()
num = y.split()



print(change_eng(num))

