class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        n=len(arr)
        for i in range(1,n):
            if arr[i-1]<arr[i]>arr[i+1]:
                return i
        return 0
