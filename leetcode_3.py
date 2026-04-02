class Solution:
    def lenofsub(self,nums):
        mx=0
        n=len(nums)
        for i in range(0,n):
            my_set=set()
            for j in range(i,n):
                if nums[j] in my_set:
                    break
                mx=max(mx,j-i+1)
                my_set.add(nums[j])
        return mx

x=input()
obj=Solution()
print(obj.lenofsub(x))