class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total_sum = sum(nums)
        
        # 1. Odd sum ho toh possible nahi
        if total_sum % 2 != 0:
            return False
            
        target = total_sum // 2
        n = len(nums)
        
        # 2. 2D DP Table initialized with -1
        # Rows: n (indices), Columns: target + 1
        dp = [[-1 for _ in range(target + 1)] for _ in range(n)]
        
        def solve(index, rem_target):
            # Base Case 1: Target ban gaya!
            if rem_target == 0:
                return True
                
            # Base Case 2: Array khatam ya target negative ho gaya
            if index >= n or rem_target < 0:
                return False
                
            # Step 1: Memoization check (kya pehle se calculate hai?)
            if dp[index][rem_target] != -1:
                return dp[index][rem_target]
                
            # Step 2: Choice 1 - TAKE (is number ko le lo)
            take = False
            if nums[index] <= rem_target:
                take = solve(index + 1, rem_target - nums[index])
                
            # Step 3: Choice 2 - SKIP (is number ko chhod do)
            skip = solve(index + 1, rem_target)
            
            # Step 4: Dono ka OR karke DP table me save karo
            dp[index][rem_target] = take or skip
            return dp[index][rem_target]
            
        return solve(0, target)