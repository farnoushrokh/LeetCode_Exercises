"""
512. Game Play Analysis II
Solved
Easy
Topics
Companies
SQL Schema
Pandas Schema
Table: Activity

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key (combination of columns with unique values) of this table.
This table shows the activity of players of some games.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday
using some device.


Write a solution to report the device that is first logged in for each player.

Return the result table in any order.

The result format is in the following example.



Example 1:

Input:
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-05-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+
Output:
+-----------+-----------+
| player_id | device_id |
+-----------+-----------+
| 1         | 2         |
| 2         | 3         |
| 3         | 1         |
+-----------+-----------+

"""
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    dates_first=activity.groupby('player_id')['event_date'].min().reset_index()
    res_merge=activity.merge(dates_first, on=['player_id', 'event_date'], how='inner')
    final=res_merge[['player_id','device_id']]
    return final

"""
/* Write your T-SQL query statement below */
with cte as
(select player_id, min(event_date) 'first_login_date' from Activity
group by player_id)
select a.player_id,  device_id from Activity a
join cte c on c.player_id = a.player_id
AND a.event_date = c.first_login_date

"""