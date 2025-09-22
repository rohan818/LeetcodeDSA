class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def is_straight(point1, point2, point3):
            (x1, y1) = point1
            (x2, y2) = point2
            (x3, y3) = point3
            return (y2-y1)*(x3-x2)==(y3-y2)*(x2-x1)

      
        point1 = coordinates[0]
        point2 = coordinates[1]
        for point in coordinates:
            if not is_straight(point1, point2, point):
                return False
        return True
