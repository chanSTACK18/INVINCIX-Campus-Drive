"""
We all know about share market. There is up and down every now and then. You are here being
asked to solve a problem of suggesting the pattern to buy and sell on the days in order to earn the
maximum profit.

You can only buy after you release and sell the share you have already purchased.
"""

# By doing most k transactions, we can get maximum profit
# Let us understand the above recurrence in the following example
# Let us say we have to buy and sell on day 1, 2, 3 and 4
# We can either buy on day 1 and sell on day 3 or buy on day 4 and sell on day 5 and buy on day 6 and sell on day 7

def maxProfit(prices):
    
    # check if the list is empty
    # if empty return 0
    if len(prices) < 2:
        return 0
    
    # initialize the max_profit to 0
    # initialize the min_price_index to 0
    min_price = 0
    max_profit = 0

    for i in range(1, len(prices)):

        # initialize the min_price to the first element of the list
        if prices[i-1] > prices[i]:
            min_price = i
        
        # check if the current element is greater than the min_price
        # if yes, then update the max_profit
        # else, do nothing
        if prices[i-1] <= prices[i] and (i +1 == len(prices) or prices[i+1] < prices[i]):

            # update the max_profit
            # print out bay and sell day
            max_profit += (prices[i] - prices[min_price])
            print(f"Shares bought at {min_price+1} and sold on Day {i+1} - {max_profit}")

    return max_profit

if __name__ == "__main__":
    # given list of prices
    prices = [165, 177, 181, 178, 202, 177, 181, 180, 189]
    print('Total Profit would be: ',maxProfit(prices))

    # Output:

    """
    Shares bought at 1 and sold on Day 3 - 16
    Shares bought at 4 and sold on Day 5 - 40
    Shares bought at 6 and sold on Day 7 - 44
    Shares bought at 8 and sold on Day 9 - 53
    Total Profit would be:  53
    """
    # Above code will print the day on which the shares are bought and sold and the profit made
    # So, Scenario 2 would be best as it gives maximum profit