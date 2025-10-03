from typing import List
class Solution:
    def maximumWealth(self, accounts:List[List[int]]) -> int:
        ans=0
        for account in accounts:
            ans = max(ans,sum(account))
        return ans


accounts = [[1, 2, 3], [3, 2, 1], [4, 5, 1]]
obj = Solution()
print(obj.maximumWealth(accounts))