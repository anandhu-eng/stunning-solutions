class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """

        nosteps = 0
        while num!=0:
            if num%2==0:
                nosteps += 1
                num = num >> 1
            else:
                nosteps += 1
                num -= 1
        
        return nosteps
