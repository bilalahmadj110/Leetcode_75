# https://leetcode.com/problems/find-pivot-index/

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        running_sum = 0
        right_sum = sum(nums)
        
        for index, i in enumerate(nums):
            right_sum -= i
            
            if right_sum == running_sum:
                return index
            running_sum += i
        return -1
        