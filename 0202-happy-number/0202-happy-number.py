class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            a = 0
            for i in str(n):
                a += int(i)**2
            n = a
        return n == 1