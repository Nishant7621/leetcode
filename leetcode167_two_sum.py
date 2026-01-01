# from typing import List

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         l = 0
#         r = len(nums) - 1

#         while l < r:
#             s = nums[l] + nums[r]

#             if s == target:
#                 return [l, r]    # indices (0-based)
#             elif s < target:
#                 l += 1
#             else:
#                 r -= 1

#         return []   # no pair found


# obj = Solution()

# nums = [-4, -1, 0, 2, 7, 8]   # SORTED list
# target = int(input("Enter your number: "))

# print(obj.twoSum(nums, target))



from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1

        while l < r:
            s = nums[l] + nums[r]

            if s == target:
                return [nums[l], nums[r]]   # return values
            elif s < target:
                l += 1
            else:
                r -= 1

        return []   # no pair found


obj = Solution()

nums = [-4, -1, 0, 2, 7, 8]   # sorted list
target = int(input("Enter your number: "))

print(obj.twoSum(nums, target))

