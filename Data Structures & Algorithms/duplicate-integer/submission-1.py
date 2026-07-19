class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numMap = {}
        size = len(nums)
        for i, n in enumerate(nums):
            if n in numMap:
                return True
            numMap[n] = i
            
        return False
        