import collections

class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        odd = False
        for i in collections.Counter(s).values():
            if i % 2 == 1:
                odd = True
                res += (i-1)
            else:
                res += i
        if odd:
            res += 1
        return res
        