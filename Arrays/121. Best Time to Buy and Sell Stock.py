#
def maxProfit(self, prices: List[int]) -> int:
    maxProfit=0
    cheapest=prices[0]
    for i in range(1,len(prices)):
        if prices[i]<cheapest:
            cheapest=prices[i]
        maxProfit=max(maxProfit, prices[i]-cheapest)
    return maxProfit
