class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        ptrA = 0
        ptrB = length -1
        result = [0] * 2
       
        while True:
            num1 = numbers[ptrA]
            num2 = numbers[ptrB]
            if num1 + num2 == target:
                result[0],result[1] = ptrA + 1, ptrB + 1
                return result
            elif num1 + num2 > target:
                ptrB -= 1
            elif num1 + num2 < target:
                ptrA += 1
            