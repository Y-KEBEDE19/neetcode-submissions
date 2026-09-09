class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hMap = {}

        for i,n in enumerate(nums):
            if n in hMap:
                return True
            
            hMap[n] = i

        return False