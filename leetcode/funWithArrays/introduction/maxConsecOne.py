class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecOne = 0
        temp = 0
        for num in nums:
            if num == 1:
                temp += 1
            else:
                if temp>consecOne:
                    consecOne = temp
                temp = 0
        if temp>consecOne:
            consecOne = temp
        return consecOne