class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        t_index = len(t) - 1
        s_index = len(s) - 1

        while t_index >= 0 or s_index >= 0:
            s_ = 0
            while s_index-s_ >= 0 and s[s_index-s_] == '#':
                s_ += 1
            s_index -= s_
            while (s_ != 0 or s[s_index] == '#') and s_index >= 0:
                if s[s_index] != '#':
                    s_ -= 1
                else:
                    s_ += 1
                s_index -= 1
            t_ = 0
            while t_index-t_ >= 0 and t[t_index-t_] == '#':
                t_ += 1
            t_index -= t_
            while (t_ != 0 or t[t_index] =='#') and t_index >= 0:
                if t[t_index] != '#':
                    t_ -= 1
                else:
                    t_ += 1
                t_index -= 1
            if t_index == s_index and t_index < 0:
                return True
            if (t_index < 0 and s_index >= 0)  or (s_index < 0 and t_index >= 0) or s[s_index] != t[t_index]:
                return False
            print ('.')
            s_index -= 1
            t_index -= 1
        return True  

            

        