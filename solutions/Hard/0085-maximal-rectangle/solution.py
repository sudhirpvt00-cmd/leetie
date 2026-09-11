# ──────────────────────────────────────────────────
# Problem  : 85. Maximal Rectangle
# Difficulty: Hard
# Tags     : Array, Dynamic Programming, Stack, Matrix, Monotonic Stack
# Link     : https://leetcode.com/problems/maximal-rectangle/
# Runtime  : 0 ms (beats 0%)
# Memory   : 12432000 (beats 0%)
# Language : python
# Copyright: (c) 2026 sudhirpvt00-cmd. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        cols = len(matrix[0])
        heights = [0] * (cols + 1)  # extra 0 at end to flush the stack
        max_area = 0

        for row in matrix:
            for i in range(cols):
                # build histogram heights: reset to 0 if '0', else increment
                heights[i] = heights[i] + 1 if row[i] == '1' else 0

            # Largest Rectangle in Histogram (monotonic stack)
            stack = [-1]
            for i in range(cols + 1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)

        return max_area