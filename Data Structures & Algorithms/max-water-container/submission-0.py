class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        res = -1 
        ptrL,ptrR = 0, length - 1

        while (ptrL < ptrR):
            numL = heights[ptrL]
            numR = heights[ptrR]

            areaH = min(numL,numR)
            areaW = ptrR - ptrL

            area = areaH * areaW

            res = max(res,area) # 

            if areaH == numL:
                ptrL += 1
            elif areaH == numR:
                ptrR -= 1

        return res

            
