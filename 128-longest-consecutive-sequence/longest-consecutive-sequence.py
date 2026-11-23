
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        longest = 0

        for num in s:
            if num - 1 not in s:
                count = 1
                current = num

                while current + 1 in s:
                    current += 1
                    count += 1

                longest = max(longest, count)

        return longest
