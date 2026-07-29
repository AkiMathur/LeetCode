class Solution:
    def fibon(self,n,f):
        if f[n] != -1:
            return f[n]
        if n <= 1: 
            return n

        f[n] = self.fibon(n-1,f)+self.fibon(n-2,f)
        return f[n]

    def fib(self, n: int) -> int:
        f = [-1] * (n+1)
        return self.fibon(n,f)