#
def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    maxCan = max(candies)
    res = []
    for i in range(len(candies)):
        res.append(candies[i] + extraCandies >= maxCan)
    return res
