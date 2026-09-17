# ──────────────────────────────────────────────────
# Problem  : 119. Pascal's Triangle II
# Difficulty: Easy
# Tags     : Array, Dynamic Programming
# Link     : https://leetcode.com/problems/pascals-triangle-ii/
# Runtime  : 0 ms (beats 100%)
# Memory   : 12352000 (beats 55%)
# Language : python
# Copyright: (c) 2026 sudhirpvt00-cmd. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1] * (rowIndex + 1)

        # Update values from right to left to reuse the same array
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] += row[j - 1]

        return row