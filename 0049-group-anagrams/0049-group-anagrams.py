from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_strs = defaultdict(list)
        result = []

        for i in strs:
            hash_strs[str(sorted(i))].append(i)
        
        for i in hash_strs.values():
            result.append(i)
        return result