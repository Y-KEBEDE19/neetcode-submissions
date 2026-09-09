class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hMap = {} # HashMap

        for i,n in enumerate(nums): # going through the loop
            if n in hMap: # check to see if the number already exists in our map
                return True
            
            hMap[n] = i # add the number as the key, and the index as the value

        return False # if we reached here, it means there are no duplicates