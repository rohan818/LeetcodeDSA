#
def convertToTitle(self, columnNumber: int) -> str:
    result = ""
    while columnNumber > 0:
        columnNumber -= 1

        remainder = columnNumber % 26
        result = chr(ord('A') + remainder) + result

        columnNumber = columnNumber // 26

    return result
