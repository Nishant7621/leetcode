class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
            
        target = total_sum // 2
        possible_sums = {0}
        
        for num in nums:

            new_sums = set()
            for s in possible_sums:
                if s + num == target:
                    return True 
                if s + num < target:
                    new_sums.add(s + num)
                    
            possible_sums.update(new_sums)
            
        return target in possible_sums