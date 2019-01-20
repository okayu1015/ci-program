data = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10,
        'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15, 'sixteen':16, 'seventeen':17,
        'eighteen':18, 'nineteen':19, 'twenty':20, 'thirty':30, 'fourty':40, 'fifty':50, 'sixty':60,
        'seventy':70, 'eighty':80,'ninety':90, 'hundred':100, 'thousand':1000}

x = input()
#x = 'fifty four thousand three hundred twelve'
x = x.split()
ans = 0
i = 0
while True:
    if i+1 < len(x) and (data[x[i+1]] == 100 or data[x[i+1]] == 1000):
        ans += data[x[i]] * data[x[i+1]]
        i += 2
    elif i+2 < len(x) and (data[x[i+2]] == 100 or data[x[i+2]] == 1000):
        ans += (data[x[i]] + data[x[i+1]]) * data[x[i+2]]
        i += 3
    else:
        ans += data[x[i]]
        i += 1
    if i >= len(x):
        break
print(ans)
