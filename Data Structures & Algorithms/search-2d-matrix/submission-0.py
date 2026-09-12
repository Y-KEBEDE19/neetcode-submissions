class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS = len(matrix), len(matrix[0])
        topR,btmR = 0,ROWS -1
        lenCol = COLS - 1
        finalRow = -1
        while topR <= btmR: 
            row = ( topR + btmR ) // 2
            if target < matrix[row][0]:
                btmR = row -1
            elif target > matrix[row][lenCol]:
                topR = row + 1
            else:
                break
        
        if not (topR<=btmR):
            return False
        
        row = (topR + btmR ) // 2

        ptrL,ptrR = 0,lenCol
        finalCol = -1
        while ptrL<= ptrR:
            mid = ( ptrL + ptrR ) // 2
            if target < matrix[row][mid]:
                ptrR = mid -1
            elif target > matrix[row][mid]:
                ptrL = mid + 1
            else:
                finalCol = mid
                return True

        print (matrix[finalRow][finalCol])
        return False