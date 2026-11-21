# ──────────────────────────────────────────────────
# Problem  : 65. Valid Number
# Difficulty: Hard
# Tags     : String
# Link     : https://leetcode.com/problems/valid-number/
# Runtime  : 4 ms (beats 26%)
# Memory   : 12204000 (beats 62%)
# Language : python
# Copyright: (c) 2026 sudhirpvt00-cmd. All rights reserved.
# Synced by: leetie
# ──────────────────────────────────────────────────

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        seen_digit = False
        seen_exponent = False
        seen_dot = False

        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True

            elif char in ['+', '-']:
                # Signs are only valid at the very start or immediately after 'e'/'E'
                if i > 0 and s[i - 1] not in ['e', 'E']:
                    return False

            elif char in ['e', 'E']:
                # Exponents require a preceding digit and cannot appear twice
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                # Reset seen_digit because an integer MUST follow the exponent
                seen_digit = False

            elif char == '.':
                # Dots cannot appear twice or anywhere after an exponent
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True

            else:
                # Any other character (e.g., 'a', 'f') is invalid
                return False

        return seen_digit