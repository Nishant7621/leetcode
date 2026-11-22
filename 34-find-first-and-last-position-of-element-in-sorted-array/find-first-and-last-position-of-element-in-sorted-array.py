class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # Helper function to find left or right boundary
        def binary_search(find_first: bool) -> int:
            left, right = 0, len(nums) - 1
            index = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    index = mid  # Found target, save this position!
                    
                    if find_first:
                        # Keep looking to the LEFT for an earlier occurrence
                        right = mid - 1
                    else:
                        # Keep looking to the RIGHT for a later occurrence
                        left = mid + 1
                        
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            return index

        # Run binary search twice
        first = binary_search(find_first=True)
        last = binary_search(find_first=False)
        
        return [first, last]