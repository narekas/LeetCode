# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.


class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        num = x
        orig = 0

        while num:
            orig = orig * 10 + num % 10
            num //= 10

        return x == orig
