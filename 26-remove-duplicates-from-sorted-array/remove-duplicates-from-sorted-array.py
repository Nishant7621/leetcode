class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = sorted(set(nums))

        for i in range(len(n)):
            nums[i] = n[i]

        return len(n)
        # n=len(nums)
        # start=0
        # for i in range(1,n):
        #     if nums[i]!=nums[start]:
        #         start+=1
        #         nums[start]=nums[i]
        # return start+1
  # <--- must return integer k, NOT a list