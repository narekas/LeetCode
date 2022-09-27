class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        pre_sum = 1
        post_sum = 1
        for i in range(len(nums)):
            ans.append(pre_sum)
            pre_sum *= nums[i]
        for j in range(len(nums)-1, -1, -1):
            ans[j] *= post_sum
            post_sum *= nums[j]
        return ans