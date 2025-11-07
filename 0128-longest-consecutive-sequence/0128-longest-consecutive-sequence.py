class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0

        a = sorted(nums)
        b = c = 1
        for i in range(len(a)-1):
            if a[i] + 1 == a[i+1]:
                c += 1
                if c > b:
                    b = c  
            elif a[i] == a[i+1]:
                continue
            else:
                c = 1
                
        
        return b