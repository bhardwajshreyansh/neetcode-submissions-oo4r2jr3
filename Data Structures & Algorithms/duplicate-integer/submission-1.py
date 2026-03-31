class Solution:
    def hasDuplicate(self, nums: List[int]) -> int:
        seen = set() #intialise a set 

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False

"""
for i in range(nums):
    for num in enumerate nums:
        if num[i] == set():
            return true
        else:
            set.append(num)
    return false


    def has_duplicates(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

"""