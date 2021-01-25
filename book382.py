a = list(input())
b = list(input())
count = 0

if len(a) > len(b):
    tmp = a
    a = b
    b = tmp

i = 0
j = 0
lena = len(a)
while True:
    if j >= len(b):
        break
    if a[i] == b[j]:
        i += 1
        j += 1
    else:
        count += 1
        j += 1
        if lena < len(b):
            lena += 1
        else:
            i += 1
    
print(count)
            