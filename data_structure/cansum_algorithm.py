"""
Write a function `canSum(targetSum, numbers)` that takes in a targetSum and an array of numbers as arguments

The function should return a boolean indicating whether or not it is possible to generate the targetSum using numbers
from the array.

You may use an element of the array as many times as needed

"""


def canSum(targetSum, numbers):
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False

    for num in numbers:
        def remainder():
            return targetSum - num

        if canSum(remainder(), numbers):
            return True
    return False


print(canSum(targetSum=7, numbers=[3, 4, 7, 5]))
