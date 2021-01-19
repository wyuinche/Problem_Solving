VER, HOR = 0, 1
BUILD_REMOVE, BUILD_SET = 0, 1

def ver(building, x, y, n):
    for b in building:
        if b[0] == x and b[1] == y and b[2] == VER:
            return True
    return False

def hor(building, x, y, n):
    for b in building:
        if b[0] == x and b[1] == y and b[2] == HOR:
            return True
    return False

def isAvailable(building, x, y, a, b, n):
    if a == VER:
        if y == 0:
            return True
        elif y == n:
            return False
        elif ver(building, x, y-1, n) or hor(building, x-1, y, n) or hor(building, x, y, n):
            return True
        else:
            return False
    elif a == HOR:
        if y == 0:
            return False
        elif x == n:
            return False
        elif ver(building, x, y-1, n) or ver(building, x+1, y-1, n) or (hor(building, x-1, y, n) and hor(building, x+1, y, n)):
            return True
        else:
            return False
    else:
            return False
 

def isIndex(building, x, y, a):
    for i in range(len(building)):
        if building[i][0] == x and building[i][1] == y and building[i][2] == a:
            return i
    return -1

# def printInfo(x, y, a, b):
#     print(x, y, end=" ")
#     if a == HOR:
#         print("HOR", end=" ")
#     else:
#         print("VER", end=" ")
#     if b == BUILD_SET:
#         print("BUILD_SET", end=" ")
#     else:
#         print("BUILD_REMOVE", end=" ")

def solution(n, build_frame):
    answer = []
    
    for build in build_frame:
        x, y, a, b = build
        if b == BUILD_REMOVE:
            i = isIndex(answer, x, y, a)
            del answer[i]
            if a == HOR:
                if hor(answer, x-1, y, n):
                    if not isAvailable(answer, x-1, y, HOR, BUILD_SET, n):
                        answer.append([x, y, a])
                if hor(answer, x+1, y, n):
                    if not isAvailable(answer, x+1, y, HOR, BUILD_SET, n):
                        answer.append([x, y, a])
                if ver(answer, x, y, n):
                    if not isAvailable(answer, x, y, VER, BUILD_SET, n):
                        answer.append([x, y, a])
                if ver(answer, x+1, y, n):
                    if not isAvailable(answer, x+1, y, VER, BUILD_SET, n):
                        answer.append([x, y, a])
            elif a == VER:
                if hor(answer, x, y+1, n):
                    if not isAvailable(answer, x, y+1, HOR, BUILD_SET, n):
                        answer.append([x, y, a])
                if hor(answer, x-1, y+1, n):
                    if not isAvailable(answer, x-1, y+1, HOR, BUILD_SET, n):
                        answer.append([x, y, a])
                if ver(answer, x, y+1, n):
                    if not isAvailable(answer, x, y+1, VER, BUILD_SET, n):
                        answer.append([x, y, a])
        elif b == BUILD_SET:
            if isAvailable(answer, x, y, a, b, n):
                answer.append([x, y, a])

    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    
    return answer