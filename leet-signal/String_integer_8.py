# Version 1 
class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s.strip()) == 0:
            return 0
        l = list(s.strip())
        sign = -1 if l[0] == '-' else 1
        
        if l[0] in ['+','-']:
            del(l[0])
        res, i = 0, 0
        
        while i < len(l) and l[i].isdigit():
            res = res * 10 + ord(l[i]) - ord('0')
            i += 1
        
        return max(-2**31, min(sign * res, 2**31-1))
    
    
# Version 2
class Solution:
    def myAtoi(self, s: str) -> int:
        digits = "0123456789+-"
        if s == "":
            return 0
        n = len(s)
        for i in range(n):
            if s[i] != " ":
                s = s[i:]
                break
        
        num = ""
        for ch in s:
            if ch not in digits:
                break
            num += ch
        
        if num == "":
            return 0
        
        num = int(num)
        return 2**31-1 if num >= 2**31-1 else (-2)**31 if num <= (-2)**31 else num        
