#
def convertToTitle(self, columnNumber: int) -> str:
    result = ""
    while columnNumber > 0:
        # Subtract 1 to make it 0-indexed (A=0, B=1, ..., Z=25)
        columnNumber -= 1

        remainder = columnNumber % 26

        # Convert remainder to corresponding letter
        result = chr(ord('A') + remainder) + result
        
        # Move to the next position
        columnNumber = columnNumber // 26

    return result
