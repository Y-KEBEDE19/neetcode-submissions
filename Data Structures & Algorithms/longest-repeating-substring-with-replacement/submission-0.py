class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Neetcode Solution: 

        l = 0
        char_map = {}
        res = 0
        for r in range(len(s)):
            char_map[s[r]] = 1 + char_map.get(s[r],0) # adding freq to our char_map

            # if replacements bigger than allowed (k), decrease window size

            while r - l + 1 - max(char_map.values()) > k:
                char_map[s[l]] -= 1
                l+= 1

            res = max(res, r - l + 1)


        return res
