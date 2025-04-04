"""
Easy
1.9K
96
company
eBay
company
Google
company
Amazon
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend
 all meetings.



Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: true


Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti < endi <= 106

"""

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1 ,len(intervals)):
            if intervals[ i -1][1] > intervals[i][0]:
                return False
        return True

