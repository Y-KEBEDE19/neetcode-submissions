class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # this is the sliding window technique:

        # we can have two pointers:
        # a left pointer and a right pointer
        # left pointer: starts at first char, and right pointer is one ahead
        # if the char at the right ptr is in the current set
        # then we increment the left pointer until that char
        # at each iteration we compute the max lengthOfLongestSubstring

        # Edge Case: length is 1
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        left, right = 0, 1
        length = len(s)
        charSet = {s[left]}
        longest = 0
        while right < length:
            new_char = s[right]
            while new_char in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])    
            longest = max(longest, (right - left) + 1)
            right += 1
        return longest
