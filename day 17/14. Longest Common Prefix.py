
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        common = len(strs[0])

        for index, str in enumerate(strs[1:]):
            last = strs[index]
            upto = min(common, len(str))
            j = 0
            while j < upto and last[j] == str[j]:
                common = j + 1
                j += 1
            if j == 0:
                return ""

        return strs[0][:common]