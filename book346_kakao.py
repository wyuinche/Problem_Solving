def solution(p):
    answer = ''

    if p == '':
        return ''
    w = p
    answer = makeCorrect(w)

    return answer


def makeCorrect(w):
    if w == '':
        return ''
    u, v = split(w)
    if isCorrect(u):
        u += makeCorrect(v)
        answer = u
    else:
        answer = '(' + makeCorrect(v) + ')' + makeOpposite(u[1:-1])
    return answer


def makeOpposite(w):
    result = ''
    for c in w:
        if c == '(':
            result += ')'
        else:
            result += '('
    return result


def split(w):
    left_n = 0
    right_n = 0
    idx = 0
    for c in w:
        idx += 1
        if c == '(':
            left_n += 1
        elif c == ')':
            right_n += 1
        if left_n == right_n:
            return w[:idx], w[idx:]


def isCorrect(u):
    stack = []
    for c in u:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                return False
            stack.pop()
    return True
