# https://leetcode.com/problems/isomorphic-strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # O(n)
        # two side hashmap
        if len(s) != len(t):
            return False
        dct = {}
        l_dct = {}
        for index in range(len(s)):
            f = s[index]
            s_ = t[index]
            if (f in dct and dct[f] != s_) or (s_ in l_dct and l_dct[s_] != f):
                return False
            dct[f] = s_
            l_dct[s_] = f
        return True
        
        
if __name__ == "__main__":
    print (Solution().isIsomorphic("foo", "bar")) # False
    print (Solution().isIsomorphic("egg", "add")) # True
    print (Solution().isIsomorphic("paper", "title")) # True