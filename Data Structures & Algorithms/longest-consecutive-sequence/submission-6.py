class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        current_length = 1
        longest = 1
        if not num_set:
            return 0

        for n in num_set: 
            start = n
            current_length = 1
            if n - 1 not in num_set:
                while (n + 1) in num_set:
                    n += 1
                    current_length += 1
                longest = max(longest,current_length)
            
        return longest
                
        