class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        best = 0

        for row in matrix:
            for c in range(cols):
                heights[c] = heights[c] + 1 if row[c] == "1" else 0

            stack = []
            for c in range(cols + 1):
                height = heights[c] if c < cols else 0

                while stack and heights[stack[-1]] > height:
                    h = heights[stack.pop()]
                    left = stack[-1] if stack else -1
                    width = c - left - 1
                    best = max(best, h * width)

                stack.append(c)

        return best