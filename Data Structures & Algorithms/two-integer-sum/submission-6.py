class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array = []
        for i, val in enumerate(nums): #for that index, value in nums
            array.append([val, i])
        array.sort()  #List use append method but sets uses add method
        i, j = 0, len(nums) - 1
        while i < j:
            curr = array[i][0] + array[j][0]

            if curr == target:
                return [
                    min(array[i][1], array[j][1]),
                    max(array[i][1], array[j][1])
                ]
            elif curr < target:
                i += 1
            else: j -= 1
