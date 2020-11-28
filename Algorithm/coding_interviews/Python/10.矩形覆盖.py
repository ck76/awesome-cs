# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number <= 0 :
            return 0
        dp = [0,1,2]
        for i in range(3,number+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[number]