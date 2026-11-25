class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        
        def ways(i: int) -> int:
            if i <= 2:
                return i

            if dp[i] != -1:
                return dp[i]
                
            dp[i] = ways(i - 1) + ways(i - 2)
            return dp[i]
            
        return ways(n)