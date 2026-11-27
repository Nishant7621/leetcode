class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        
        # (m + 1) x (n + 1) table with infinity
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        
        # Base case: Princess room se bahar nikalte waqt at least 1 health chahiye
        dp[m][n - 1] = 1
        dp[m - 1][n] = 1
        
        # Peechhe se (Bottom-Right se Top-Left) loop chalao
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                needed_next = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(1, needed_next - dungeon[i][j])
                
        # Starting point par minimum required health
        return dp[0][0]