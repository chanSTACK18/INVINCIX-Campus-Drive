"""
We all know about share market. There is up and down every now and then. You are here being
asked to solve a problem of suggesting the pattern to buy and sell on the days in order to earn the
maximum profit.

You can only buy after you release and sell the share you have already purchased.
"""

# By doing most k transactions, we can get maximum profit
# Let us understand the above recurrence in the following example
# Let us say we have to buy and sell on day 1, 2, 3 and 4
# We can either buy on day 1 and sell on day 3 or buy on day 4 and sell on day 5


def maxProfit(price, n, k):

    # Table to store results of subproblems
    # profit[t][i] stores maximum profit
    # using at most t transactions up to
    # day i (including day 1)
    profit = [[0 for i in range(n + 1)] for j in range(k + 1)]

    # Fill the table in bottom-up manner
    # Note that the table is filled in a slightly
    # day and for each day, we can either buy or sell
    for i in range(1, k + 1):
        prevDiff = float('-inf')
        # For first transaction, we need to find the difference between
        for j in range(1, n):
            prevDiff = max(prevDiff,profit[i - 1][j - 1] -price[j - 1])
            profit[i][j] = max(profit[i][j - 1],price[j] + prevDiff)

    return profit[k][n - 1]

# Driver Code
if __name__ == "__main__":
    # k time given stack of n days
    # Example enter 3 transactions
    k = int(input("Enter the number of transactions: "))
    prices = [165, 177, 181, 178, 202, 177, 181, 180, 189]
    n = len(prices)
    print("Maximum profit is:",maxProfit(prices, n, k))

# Output:

# if k = 3 max profit is: 52
# if k = 4 max profit is: 53

# if k = 4 Scenario 2 would be best as it gives maximum profit