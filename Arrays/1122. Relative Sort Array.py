# 1122. Relative Sort Array

def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    m = sorted([i for i in arr1 if i not in arr2])
    res = []
    for i in arr2:
        x = arr1.count(i)
        for j in range(x):
            res.append(i)
    for i in m:
        res.append(i)
    
    return res
