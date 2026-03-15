from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        return nums[0]


obj = Solution()
nums = [4,5,6,7,0,1,2]
print(obj.findMin(nums))