from bisect import bisect_left
from bisect import bisect_right
from bisect import bisect

Q_BEFORE, Q_AFTER = 0, 1

        
def findIdx(words, string):
    incString = string[:-1] + chr(ord(string[-1])+1)
    start = bisect_left(words, string)
    end = bisect_right(words, incString) - 1
    return start, end
    

def findWords(words, query):
    answer = 0
    query_list = list(query)
    query_len = len(query)
    quest_len = query_list.count('?')
    string = query[:-quest_len]
    string_len = len(string)
    
    if query_len == quest_len:
        for i in words:
            if len(words[i]) == query_len:
                answer += 1
        return answer
    
    
    start, end = findIdx(words, string)
    # print(words)
    # print(start, end, query)
    if start == end:
        if len(words[start]) != query_len:
            return 0
        if words[start][:-quest_len] == string:
            return 1
        else:
            return 0
    for i in range(start, end+1):
        if len(words[i]) != query_len:
            continue
        if words[i][:-quest_len] == string:
            answer += 1
    
    return answer

def queryStyle(query):
    if query[0] == '?':
        return Q_BEFORE
    else:
        return Q_AFTER


def solution(words, queries):
    answer = []
    
    words.sort()
    words_reversed = sorted(words, key=lambda x: x[::-1])
    for i in range(len(words)):
        words_reversed[i] = words_reversed[i][::-1]
    
    for q in queries:
        if queryStyle(q) == Q_AFTER:
            answer.append(findWords(words, q))
        else:
            answer.append(findWords(words_reversed, q[::-1]))
    
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))