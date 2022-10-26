# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        mid = 1
        while left <= right:
            mid = (left + right) // 2
            if self.isBadVersion(mid):
                right = mid - 1
                if not self.isBadVersion(right):
                    return mid
            else:
                left = mid + 1
        return mid
    
    def isBadVersion(version: int) -> bool:
        return True