#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        n = len(arr)
        left = 0
        curr_sum = 0
        
        for right in range(n):
            curr_sum += arr[right]  # expand window by adding right element
            
            # shrink window from left if sum exceeds target
            while curr_sum > target and left <= right:
                curr_sum -= arr[left]
                left += 1
            
            # check if we found the target sum
            if curr_sum == target:
                return [left + 1, right + 1]  # convert to 1-based indexing
        
        # if no subarray found
        return [-1]