from random import randint
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8]

s = "how does it pick a number?"

n = ""


while len(n) < 13:
    r = randint(-10009000 , 10009000)
    if r < len(digits) - 1 and r > -1:
        n += str(digits[r])

with open("out2.txt", 'w+') as f:
    f.write(n)

print(n)
