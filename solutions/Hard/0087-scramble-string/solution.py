# ──────────────────────────────────────────────────
# Problem  : 87. Scramble String
# Difficulty: Hard
# Tags     : String, Dynamic Programming
# Link     : https://leetcode.com/problems/scramble-string/
# Runtime  : 23 ms (beats 28%)
# Memory   : 12480000 (beats 95%)
# Language : python
# Copyright: (c) 2026 sudhirpvt00-cmd. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def __init__(self):
        self.memo = {}

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # Base Cases
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):  # Anagram check pruning
            return False
        
        state = (s1, s2)
        if state in self.memo:
            return self.memo[state]
        
        n = len(s1)
        for i in range(1, n):
            # Case 1: No Swap
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                self.memo[state] = True
                return True
            
            # Case 2: Swap
            if self.isScramble(s1[:i], s2[n - i:]) and self.isScramble(s1[i:], s2[:n - i]):
                self.memo[state] = True
                return True

        self.memo[state] = False
        return False