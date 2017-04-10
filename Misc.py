import sys

def getMaxProfit(M, profit, city, visit):
    """This function gets the max profit"""
    items = [[] for i in range(M)]
    size = len(profit)
    for i in range(size):
        items[city[i] - 1].append(profit[i])

    for i in range(M):
        items[i] = sorted(items[i], reverse = True)
    profit = 0
    for c in visit:
        if len(items[c - 1]):
            profit += items[c - 1][0]
            items[c - 1].pop(0)
    return profit

