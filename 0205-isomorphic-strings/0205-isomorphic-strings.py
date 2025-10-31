from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = defaultdict(list)
        t_dict = defaultdict(list)

        for i in range(len(s)):
            s_dict[s[i]].append(i)
        for i in range(len(t)):
            t_dict[t[i]].append(i)

        s_values = [i for i in s_dict.values()]
        t_values = [i for i in t_dict.values()]

        if (s_values == t_values):
            return True
        else:
            return False
