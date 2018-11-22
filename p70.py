class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        from functools import lru_cache
        @lru_cache(128)
        def fib(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            return fib(n - 1) + fib(n - 2)
        return fib(n)
            