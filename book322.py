string = list(input())
string.sort()
print(string)

start_ascii = ord('A')
idx = 0
for i in range(26):
    idx = string.index(chr(start_ascii + i))
    if idx >= 0:
        break

if idx == 0:
    print("".join(string))
elif idx < 0:
    tmp = [int(x) for x in string]
    print(sum(tmp))
else:
    print("".join(string[idx:]), end='')
    tmp = [int(x) for x in string[:idx]]
    print(sum(tmp))