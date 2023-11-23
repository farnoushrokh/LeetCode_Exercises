"""
Easy
8.7K
861
company
Amazon
company
Facebook
company
Bloomberg
Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.


Some new explanation on solving this issue
In Python, the ^ operator is used for bitwise XOR (exclusive OR) operation. It takes two binary numbers and returns
 a new binary number by performing the XOR operation on corresponding bits.

Here's the bitwise XOR operation for 6 and 3 in binary:

6 in binary: 110
3 in binary: 011
Now, let's perform the XOR operation bit by bit:

1 XOR 0 gives 1
1 XOR 1 gives 0
0 XOR 1 gives 1
So, the result of 110 XOR 011 is 101 in binary, which is equal to 5 in decimal.

That's why print(6 ^ 3) in Python returns 5. It's important to note that ^ is a bitwise operator,
not the exponentiation operator. If you want to calculate the power, you should use ** instead of ^.

"""
