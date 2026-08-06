class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}
        for i,n in enumerate(nums):
            if n in duplicate:
                return True
            duplicate[n] = i
            

        return False
            
        