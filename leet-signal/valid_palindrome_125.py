class Solution:
    def isPalindrome(self, s: str) -> bool:
        return [i for i in s.lower() if i.isalnum()] == [i for i in s[::-1].lower() if i.isalnum()]
