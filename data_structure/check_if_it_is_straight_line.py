"""
Easy
2.5K
264
company
Amazon
company
Apple
company
Palantir Technologies
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
 Check if these points make a straight line in the XY plane.





Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:



Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false


"""

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[: 2]
        for x, y in coordinates:
            if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
                return False
        return True