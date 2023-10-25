from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Keep track of visited 
        visited = []
        # Create a stack of cities to visit
        to_visit = [0]
        # read left to right along the city's row
        # add to visited,
        to_visit = [] # no more to visit
        # Add city to visit to stack of to_visit
        to_visit = [0]
        count = 0

        while to_visit:
            # for a given row, if visit_city returns empty, increment province count and move to next row
            # else, call visit_city on to_visit
            # if to_visit is empty -> count province += 1
            # if there are more cities in isConnected, add the next un-visited city to to_visit
            pass

        return count
    
    def visit_city(self, city:int, connections: List[int], visited):
        to_visit = []
        # If a node is not in visited and is 1, add to to_visit.

        return to_visit

matrix0 = [
    [1,1,0],
    [1,1,0],
    [0,0,1]
]

matrix1 = [
    [1,1,0],
    [1,1,0],
    [0,0,1]
]