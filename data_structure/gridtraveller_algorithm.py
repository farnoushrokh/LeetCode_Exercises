memo = {}


def grid_traveller(m, n):
    def key():
        return m + ',' + n
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[key] = grid_traveller(m - 1, n) + grid_traveller(m, n - 1)
    return memo[key]


print(grid_traveller(m=3, n=3))
