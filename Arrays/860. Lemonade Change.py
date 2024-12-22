# Lemonade Change
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        l = []
        for i in bills:
            if i == 5:
                l.append(i)
            elif i == 10:
                if l.count(5) == 0:
                    return False
                l.append(i)
                l.remove(5)
            else:
                if l.count(5) == 0:
                    return False
                elif l.count(10) == 0:
                    if l.count(5) < 3:
                        return False
                    l.remove(5)
                    l.remove(5)
                    l.remove(5)
                    continue
                else:
                    l.remove(10)
                    l.remove(5)
        return True
