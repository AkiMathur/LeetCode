from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d_i = defaultdict(list)

        for i in range(len(nums)):
            if nums[i] in d_i:
                for j in d_i[nums[i]]:
                    if abs(j-i) <= k:
                        return True
            d_i[nums[i]].append(i)

        return False