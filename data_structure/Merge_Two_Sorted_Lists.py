"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next


"""
solution:
Linkedlists can be confusing especially if you've recently started to code but (I think) once you understand it fully,
it should not be that difficult.

For this problem, I'm going to explain several ways of solving it BUT I want to make something clear. Something that 
you've seen a lot of times in the posts on this website but probably haven't fully understood. dummy variable! It has 
been used significantly in the solutions of this problem and not well explained for a newbie level coder! The idea is
we're dealing with pointers that point to a memory location! Think of it this way! You want to find gold that is 
hidden somewhere. Someone has put a set of clues in a sequence! Meaning, if you find the first clue and solve 
the problem hidden in the clue, you will get to the second clue! Solving the hidden problem of second clue will get you
to the thrid clue, and so on! If you keep solving, you'll get to the gold! dummy helps you to find the first clue!!!!

Throughout the solution below, you'll be asking yourself why dummy is not changing and we eventually return dummy.
next???? It doesn't make sense, right? However, if you think that dummy is pointing to the start and there is another
variable (temp) that makes the linkes from node to node, you'll have a better filling!
Similar to the gold example if I tell you the first clue is at location X, then, you can solve clues sequentially 
(because of course you're smart) and bingo! you find the gold! Watch this.

This video shows why we need the dummy! Since we're traversing using temp but once temp gets to the tail of the sorted 
merged linkedlist, there's no way back to the start of the list to return as a result! So dummy to the rescue! 
it does not get changed throughout the list traversals temp is doing! So, dummy makes sure we don't loose the head of 
the thread (result list). Does this make sense? Alright! Enough with dummy!

I think if you get this, the first solution feels natural! Now, watch this. You got the idea?? Nice!

First you initialize dummy and temp. One is sitting at the start of the linkedlist and the other (temp) is going to 
move forward find which value should be added to the list. Note that it's initialized with a value 0 but 
it can be anything! You initialize it with your value of choice! Doesn't matter since we're going to finally return
dummy.next which disregards 0 that we used to start the linkedlist. Line #1 makes sure none of the l1 and l2 are empty!
If one of them is empty, we should return the other! If both are nonempty, we check val of each of them to add 
the smaller one to the result linkedlist! In line #2, l1.val is smaller and we want to add it to the list. How? 
We use temp POINTER (it's pointer, remember that!). Since we initialized temp to have value 0 at first node,
we use temp.next to point 0 to the next value we're going to add to the list l1.val (line #3). Once we do that,
we update l1 to go to the next node of l1. If the if statement of line #2 doesn't work, we do similar stuff with l2.
And finally, if the length of l1 and l2 are not the same, we're going to the end of one of them at some point! 
Line #5 adds whatever left from whatever linkedlist to the temp.next (check the above video for a great explanation
of this part). Note that both linkedlists were sorted initially. Also, this line takes care of when one of the
linkedlists are empty. Finally, we return dummy.next since dummy is pointing to 0 and next to zero is

"""