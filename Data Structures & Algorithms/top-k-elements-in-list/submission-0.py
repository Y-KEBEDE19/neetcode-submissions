class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        output = []
        for num in nums:
            if num in map.keys():
                map[num] += 1
            else:
                map[num] = 1
        
        for i in range(k):
            ctr = 0
            largestNum = -1
            for key in map:
                if map[key] >= ctr:
                    ctr = map[key]
                    largestNum = key
            del map[largestNum]
            output.append(largestNum)
            
        return output

        