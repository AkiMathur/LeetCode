class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        hash_p = dict()
        str_p = []

        if len(pattern) != len(s):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in hash_p.keys():
                if s[i] not in hash_p.values():
                    hash_p[pattern[i]] = s[i]
                else:
                    return False 

        for i in pattern:
            str_p.append(hash_p[i])
        

        if str_p == s:
            return True
        else:
            return False