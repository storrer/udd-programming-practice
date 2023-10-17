"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8 Output = 4
k = 6
can_eat_all == True
right = guess - 1
guess = (left + right) // 2

k = 3
can_eat_all == False
left = guess + 1
guess = (left + right) // 2 # 4

k = 4
can_eat_all == True
left = guess + 1



left = 1
right = max(piles)
guess = (left + right) // 2
if can_eat_all(guess) == True:
    right = guess - 1
if can_eat_all == False:



Output: 


Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 
"""
from typing import List


class Solution:
    def can_eat_all(self, speed, time_allotted, piles):
        total_time_required = 0
        for pile in piles:
            time_required = (pile + speed - 1) // speed # Integer division rounded up
            total_time_required += time_required
        
        return total_time_required <= time_allotted

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            guess = (left + right) // 2

            if self.can_eat_all(guess, h, piles):
                right = guess 
            else:
                left = guess + 1
        
        return right
    
piles1 = [3,6,7,11]
h1 = 8
piles2 = [30,11,23,4,20]
h2 = 5
h3 = 6


sol = Solution()
print(sol.minEatingSpeed(piles1, h1))
print(sol.minEatingSpeed(piles2, h2))
print(sol.minEatingSpeed(piles2, h3))
