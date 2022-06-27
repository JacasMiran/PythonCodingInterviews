# Given N bulds, eiter on (1) or off (0).
# Turning on ith buld causes all remaining bulbs on
# to the right to flip

# Find the min number of swithches to turn all the
# bulbs on.

# Constraints:
# 1<=N <=1e5
# A[i]= {0,1} 

class Solution:
    def bulbs(self, A):
        cost = 0

        for b in A:
            if cost % 2==0:
                b=b
            else:
                b = not b
            
            if b % 2 == 1:
                continue
            else:
                cost += 1
        return cost