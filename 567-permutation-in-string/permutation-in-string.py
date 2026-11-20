class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n1 = len(s1)
        n2 = len(s2)
        
        # If s1 is longer than s2, s2 cannot contain a permutation of s1
        if n1 > n2:
            return False
        
        # 1. Sort s1 once
        sorted_s1 = sorted(s1)
        
        # 2. Check every window of length n1 in s2
        for i in range(n2 - n1 + 1):
            window = s2[i : i + n1]
            
            # Sort the current window and check if it matches sorted_s1
            if sorted(window) == sorted_s1:
                return True
                
        return False