class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqList = []
        for num in nums:
            sqList.append(num*num)
        sqList.sort()
        return sqList