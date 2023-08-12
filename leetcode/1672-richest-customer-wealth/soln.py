class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        highestWealth = 0
        for customer in accounts:
            temp = 0
            for moneyDeposit in customer:
                temp += moneyDeposit
            if temp > highestWealth:
                highestWealth = temp

        return highestWealth
