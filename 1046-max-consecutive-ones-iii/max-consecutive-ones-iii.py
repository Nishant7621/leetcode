class Solution(object):
    def longestOnes(self, nums, k):
        l = 0
        r = 0
        zeros = 0
        length = 0

        while r < len(nums):
            if nums[r] == 0:
                zeros += 1

            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            length = max(length, r - l + 1)
            r += 1

        return length