# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # O(len(t))
        l = 0
        last = 0
        for first in s:
            for index, second in enumerate(t[last:], start=last):
                l += 1
                if first == second:
                    last = index + 1
                    break
            else:
                return False
        print (l)
        return True
        

if __name__ == "__main__":
    print (Solution().isSubsequence("abc", "ashsaaavavavavavvavabc"))
    print (Solution().isSubsequence("axc", "ahbgdc"))