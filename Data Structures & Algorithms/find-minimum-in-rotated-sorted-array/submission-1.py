class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # NeetCode Solution: 

        length = len (nums) # length of nums

        left_ptr, right_ptr = 0, length - 1 # two pointers

        
            
        res = nums[0] 
        while left_ptr <= right_ptr:
        # At any point to see if already sorted
            if nums[right_ptr] > nums[left_ptr]:
                res = min(res,nums[left_ptr])
                break

            mid = (left_ptr + right_ptr) // 2 # Finding our mid
            res = min(res,nums[mid])
            if nums[mid] >= nums[left_ptr]: # Then they are in the same 
                left_ptr = mid + 1 # we want to search the right_ptr
            else:
                right_ptr = mid - 1 # we want to search the left

        return res
