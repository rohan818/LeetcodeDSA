#
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        persons = list(zip(heights, names))
        persons.sort(reverse=True, key=lambda x:x[0])
        sorted_names = [name for height, name in persons]
        return sorted_names
