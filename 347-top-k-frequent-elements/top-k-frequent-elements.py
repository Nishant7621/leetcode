class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        unique_nums = set(nums)
        return sorted(unique_nums, key=nums.count, reverse=True)[:k]