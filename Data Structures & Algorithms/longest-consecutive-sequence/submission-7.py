class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # after getting hints but no direct coding solution: 

        hash_set = set(nums)


        count = 1
        maxLength = 0
        for n in nums:
            curr_num = n
            count = 1
            if n - 1 not in hash_set:
                while curr_num+1 in hash_set:
                    count += 1
                    curr_num += 1
            
            maxLength = max(maxLength, count)
            
        return maxLength

