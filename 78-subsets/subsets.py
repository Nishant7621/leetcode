class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []

        def backtrack(index):
            # Store current subset
            ans.append(subset[:])

            # Try all remaining elements
            for i in range(index, len(nums)):
                subset.append(nums[i])      # Choose
                backtrack(i + 1)            # Explore
                subset.pop()                # Backtrack

        backtrack(0)
        return ans