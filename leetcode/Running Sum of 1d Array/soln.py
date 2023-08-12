class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = 0
        returnList = []
        for i in range(len(nums)):
            sum += nums[i]
            returnList.append(sum)

        return returnList
