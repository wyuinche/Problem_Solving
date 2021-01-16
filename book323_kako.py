def solution(s):
    answer = 0
    
    slen = len(s)
    min = slen
    for i in range(1, slen):
        cur = compress(s, slen, i)
        if cur < min:
            min = cur
    answer = min
    return answer

def compress(s, slen, n):
    repeat = slen // n
    left = slen % n
    result = ""
    
    sbefore = s[:n]
    count = 1
    result += sbefore
    for i in range(1, repeat):
        scurr = s[i*n:(i+1)*n]
        if sbefore == scurr:
            count += 1
            if i == repeat-1 and count != 1:
                result += str(count)
            continue
        if count != 1:
            result += str(count)
        result += scurr
        sbefore = scurr
        count = 1
    return len(result) + left
