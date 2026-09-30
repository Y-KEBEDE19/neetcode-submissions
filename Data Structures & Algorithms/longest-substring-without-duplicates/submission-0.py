class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        # NeetCode Solution: 

        lengt_of_s = len(s)
        char_set = set()

        left_ptr = 0

        result = 0
        for right_ptr in range(lengt_of_s):

            
            while s[right_ptr] in char_set:
                char_set.remove(s[left_ptr])
                left_ptr+=1
            
            char_set.add(s[right_ptr])
            result = max(result, len(char_set))

        return result


            