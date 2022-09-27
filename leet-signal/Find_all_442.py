# Version 1
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return [key for key, values in Counter(nums).items() if values == 2]


# Version 2
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s, l = set(), []
        for n in nums:
            if n in s: l.append(n)
            else: s.add(n)
        return l
