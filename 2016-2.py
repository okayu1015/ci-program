data = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7}

#10進数をn進数へ
def change(i, n):
    if (int(i / n)):
        return change(int(i/n), n)+str(i%n)
    return str(i%n)

#n進数を10進数へ
def change_to_10(i, n):
    x = 0
    for j in range(1, len(i)+1):
        x += int(data[str(i[-j])]) * (n ** (j-1))
    return x

y = input()
print(change_to_10(str(y), 8))
