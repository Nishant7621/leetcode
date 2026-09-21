class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k
            r = num % k

            # Subarray containing only num
            new_dp[r] += 1

            # Extend previous subarrays
            for old_r in range(k):
                new_r = (old_r * r) % k
                new_dp[new_r] += dp[old_r]

            dp = new_dp

            # Add all subarrays ending at current position
            for r in range(k):
                result[r] += dp[r]

        return result