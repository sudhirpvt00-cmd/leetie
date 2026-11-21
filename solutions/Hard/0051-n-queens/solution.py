# ──────────────────────────────────────────────────
# Problem  : 51. N-Queens
# Difficulty: Hard
# Tags     : Array, Backtracking, Algorithm X
# Link     : https://leetcode.com/problems/n-queens/
# Runtime  : 10 ms (beats 96%)
# Memory   : 12420000 (beats 70%)
# Language : python
# Copyright: (c) 2026 sudhirpvt00-cmd. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        pos_diag = set()  # (r + c) is constant along positive diagonals (/)
        neg_diag = set()  # (r - c) is constant along negative diagonals (\)

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                # Place queen
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                # Remove queen (backtrack)
                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res