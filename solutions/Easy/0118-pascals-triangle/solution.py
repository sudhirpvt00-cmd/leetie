# ──────────────────────────────────────────────────
# Problem  : 118. Pascal's Triangle
# Difficulty: Easy
# Tags     : Array, Dynamic Programming
# Link     : https://leetcode.com/problems/pascals-triangle/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12360000 (beats 65%)
# Language : python
# Copyright: (c) 2026 sudhirpvt00-cmd. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []

        for i in range(numRows):
            # Each row starts with 1s and has length (i + 1)
            row = [1] * (i + 1)
            
            # Compute the inner elements using values from the previous row
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
                
            triangle.append(row)

        return triangle