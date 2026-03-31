class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #resules array to store list
        res = []
        nums.sort()
        #sorting so we don't have to check repeated values and l and r pointer can know next value is greater or smaller

        for i,a in enumerate(nums):
            #checks
            l,r = i + 1, len(nums) - 1
            
            if a > 0:
                break

            if i > 0 and a == nums[i-1]:
                continue
            
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r-=1
                elif threeSum < 0:
                    l+=1
                else:
                    res.append([a , nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return res
   
