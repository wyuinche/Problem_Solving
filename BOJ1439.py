string = list(map(int, input()))
One = 0
Zero = 0
curr = string[0]
result = 0

if curr == 0:
    Zero = 1
else:
    One = 1

for i in string[1:]:
    if i != curr:
        if i == 0:
            Zero += 1
        else:
            One += 1
        curr = i

print(min(Zero, One))
