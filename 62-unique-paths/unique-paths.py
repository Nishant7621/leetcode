class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Sirf ek row (size n) maintain karo
        row = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                row[j] = row[j] + row[j - 1]  # upar wala + left wala
        return row[n - 1]