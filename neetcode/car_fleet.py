from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = [[p,s] for p, s in zip(position, speed)]
        sorted_fleets = sorted(fleets,key=lambda x:x[0], reverse=True)


        # Calculate the time to destination for each fleet
        time_to_destination = []
        for p,s in sorted_fleets:
            time_to_destination.append((target - p) / s)
        
        # Move cars along incrementally, and doing some calculation at each point


        return 0 # Actual number pending


position = [10,8,0,5,3] # [(0,10)]

speed = [2,4,1,1,3]

target = 12
