class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans=set(nums)
        res=[]
        for i in range(1,len(nums)+1):
            if i not in ans:
                res.append(i)
        return res

        # return list(set(range(1, len(nums)+1)) - set(nums))


