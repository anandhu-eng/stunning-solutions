class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        countEvenDigit = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                countEvenDigit += 1
        return countEvenDigit
