class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix_arr,suffix_arr,res = [0] * length,[0] * length,[0] * length
        pSum,sSum = 1,1

        # if nums[0] == 0:
        #     pSum = 0
        # if nums[-1] == 0:
        #     sSum = 0
        for i in range(length): # prefix Sum
            prefix_arr[i] = pSum
            pSum *= nums[i]

        for i in range(length - 1, -1, -1): # suffix Sum
            suffix_arr[i] = sSum
            sSum *= nums[i]

        for i in range(length):
            res[i] = prefix_arr[i] * suffix_arr[i]

        return res

        
    # Trace Example #1:

    # nums = [1,2,4,6]

    # prefix_arr = [1,1,2,8]
    # suffix_arr = [48,24,6,1]

    # res = [48,24,12,8] ✅

    # Trace Example #2: 

    # nums = [-1,0,1,2,3]

    # prefix_arr = [1,-1,0,0,0]
    # suffix_arr = [0,6,6,3,1]

    # res = [0,-6,0,0,0]

