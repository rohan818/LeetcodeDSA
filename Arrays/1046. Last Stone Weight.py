#
def lastStoneWeight(self, stones: List[int]) -> int:

    def remove_largest():
        idx_largest = stones.index(max(stones))
        return stones.pop(idx_largest)

    while len(stones) > 1:
        s1 = remove_largest()
        s2 = remove_largest()
        if s1 != s2:
            stones.append(s1 - s2)
    
    return stones[0] if stones else 0
