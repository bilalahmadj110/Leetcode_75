# https://leetcode.com/problems/running-sum-of-1d-array
class Solution:
    def runningSum(self, nums):
        for index, i in enumerate(nums[1:], start=1):
            nums[index] += nums[index - 1]
        return nums
    
