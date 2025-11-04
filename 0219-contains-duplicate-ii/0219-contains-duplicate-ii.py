from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d_i = defaultdict(list)

        for i in range(len(nums)):
            d_i[nums[i]].append(i)

        for i in d_i.values():
            for j in range(len(i)):
                for l in range(j+1,len(i)):
                    if abs(i[j]-i[l]) <= k:
                        return True
        return False