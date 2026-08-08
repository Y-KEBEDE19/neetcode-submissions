class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        length = len(nums)
        for i in range(length):
            value = target - nums[i]
            if nums[i] in map:
                return [map[nums[i]],i]
            map[value] = i
            

        