#
def threeConsecutiveOdds(self, arr: List[int]) -> bool:
    cn_odds = 0
    for num in arr:
        if num % 2 == 1:
            cn_odds += 1
        else:
            cn_odds = 0

        if cn_odds == 3:
            return True

    return False
