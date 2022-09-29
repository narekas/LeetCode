def solution(s):
    while '(' in s:
        x = s.rfind('(')
        y = s.find(')', x)
        s = s[:x] + s[x+1:y][::-1] + s[y+1:]
    return s
