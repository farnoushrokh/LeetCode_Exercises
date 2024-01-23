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


print(canSum(targetSum=8, numbers=[2, 3, 5]))

# Now use memoization
memo = {}


def canSum(targetSum, numbers):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False

    for num in numbers:
        def remainder():
            return targetSum - num

        if canSum(remainder(), numbers):
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False


print(canSum(targetSum=8, numbers=[2, 3, 5]))

"""
Write a function `howSum(targetSum, numbers)` that takes in a targetSum and an array of numbers as arguments.

The function should return an array containing any combination of elements that add up to exactly the targetSum.
if there is not combination then return null
"""


def howSum(targetSum, numbers):
    if targetSum == 0:
        return 'null'
    if targetSum < 0:
        return 'null'
    for num in numbers:
        def remainder():
            return targetSum - num

        def remaindered():
            return howSum(remainder(), numbers)
        if remaindered():
            return howSum(remaindered(), num)


print(howSum(targetSum=8, numbers=[2, 3, 5]))
