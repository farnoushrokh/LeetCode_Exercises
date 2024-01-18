"""
1949. Strong Friendship
Medium
Topics
Companies
SQL Schema
Pandas Schema
Table: Friendship

+-------------+------+
| Column Name | Type |
+-------------+------+
| user1_id    | int  |
| user2_id    | int  |
+-------------+------+
(user1_id, user2_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates that the users user1_id and user2_id are friends.
Note that user1_id < user2_id.


A friendship between a pair of friends x and y is strong if x and y have at least three common friends.

Write a solution to find all the strong friendships.

Note that the result table should not contain duplicates with user1_id < user2_id.

Return the result table in any order.

The result format is in the following example.



Example 1:

Input:
Friendship table:
+----------+----------+
| user1_id | user2_id |
+----------+----------+
| 1        | 2        |
| 1        | 3        |
| 2        | 3        |
| 1        | 4        |
| 2        | 4        |
| 1        | 5        |
| 2        | 5        |
| 1        | 7        |
| 3        | 7        |
| 1        | 6        |
| 3        | 6        |
| 2        | 6        |
+----------+----------+
Output:
+----------+----------+---------------+
| user1_id | user2_id | common_friend |
+----------+----------+---------------+
| 1        | 2        | 4             |
| 1        | 3        | 3             |
+----------+----------+---------------+
Explanation:
Users 1 and 2 have 4 common friends (3, 4, 5, and 6).
Users 1 and 3 have 3 common friends (2, 6, and 7).
We did not include the friendship of users 2 and 3 because they only have two common friends (1 and 6).

"""

"""
# Write your MySQL query statement below
WITH all_friendships AS (
  SELECT F1.user1_id AS friend, F1.user2_id AS friend_with FROM Friendship F1
  UNION ALL
  SELECT F2.user2_id AS friend, F2.user1_id AS friend_with FROM Friendship F2
)
SELECT
  AF1.friend AS user1_id,
  AF2.friend AS user2_id,
  COUNT(*) AS common_friend
FROM
  all_friendships AF1
  INNER JOIN all_friendships AF2
    ON AF1.friend_with = AF2.friend_with
      AND AF1.friend < AF2.friend
WHERE
  EXISTS (SELECT 1 FROM Friendship F WHERE F.user1_id = AF1.friend AND F.user2_id = AF2.friend)
GROUP BY
  AF1.friend, AF2.friend
HAVING
  COUNT(*) >= 3;
"""

"""
import pandas as pd
import collections

def strong_friendship(friendship: pd.DataFrame) -> pd.DataFrame:
    network = collections.defaultdict(set)
    for index, row in friendship.iterrows():
        network[row['user1_id']].add(row['user2_id'])
        network[row['user2_id']].add(row['user1_id'])
    friendships_considered = set()
    output_tuples = []
    for user1_id in network.keys():
        for user2_id in network.keys():
            if user1_id == user2_id:
                continue
            elif (markov_key := tuple(sorted([user1_id, user2_id]))) in friendships_considered:
                continue
            elif markov_key[0] in network[markov_key[1]]:
                friendships_considered.add(markov_key)
                friends_of_a = network[markov_key[0]]
                friends_of_b = network[markov_key[1]]
                strength_of_friendship = len(friends_of_a.intersection(friends_of_b))
                if strength_of_friendship >= 3:
                    output_tuples.append((markov_key[0], markov_key[1], strength_of_friendship))
                else:
                    continue
            else:
                continue

    return pd.DataFrame(output_tuples, columns=['user1_id', 'user2_id', 'common_friend'])

"""
