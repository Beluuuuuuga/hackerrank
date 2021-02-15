# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    cost = 0
    num = 0

    for p in prices:
        cost += p
        if cost > k: break
        num += 1
    return num
