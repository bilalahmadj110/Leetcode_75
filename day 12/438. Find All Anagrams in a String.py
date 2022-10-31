import collections

class Solution:
    def findAnagrams(self, s: str, p: str):
        output = []

        count_p = collections.Counter(p)
        count = collections.Counter()
        
        left = 0
        for right in range(len(s)):
            char = s[right]
            
            if char in count_p:
                while count[char] >= count_p[char] and left < len(s):
                    new_char = s[left]
                    count[new_char] -= 1
                    left += 1
                count[char] += 1
                length = right - left + 1
                if length == len(p):
                    output.append(left)
            else:
                count.clear()
                left = right + 1
                
        return output