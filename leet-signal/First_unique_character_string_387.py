class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = Counter(s)
        for i, char in enumerate(s):
            if dict[char] == 1:
                return i
        return -1
