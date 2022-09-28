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
        
