class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        i = 0
    
        while i < len(intervals):
            j = i + 1
            while j < len(intervals):
            # Check if intervals[i] and intervals[j] overlap
                if intervals[j][0] <= intervals[i][1]:
                    intervals[i][1] = max(intervals[i][1], intervals[j][1])
                    intervals.pop(j)  # Remove merged interval
                else:
                    j += 1
            i += 1
        
        return intervals
        