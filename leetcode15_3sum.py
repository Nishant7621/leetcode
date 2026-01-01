from typing import List

class Solution:
    def threeSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        my_set = set()
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp=[nums[i],nums[j],nums[k]]
                        temp.sort()
                        my_set.add(tuple(temp))

        return [nums for nums in my_set]
    
# your class (already defined above)
obj = Solution()          # create object

nums = [-1, 0, 1, 2, -1, -4]
target = 0

result = obj.threeSum(nums, target)   # call method
print(result)

