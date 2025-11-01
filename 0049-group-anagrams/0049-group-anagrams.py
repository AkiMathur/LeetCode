from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_strs = defaultdict(list)
        result = []

        for i in strs:
            hash_strs[tuple(sorted(i))].append(i)

        return list(hash_strs.values())