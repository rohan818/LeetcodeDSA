#
def gcdOfStrings(self, str1: str, str2: str) -> str:
    def gcd(a, b):
        return abs(a) if b == 0 else gcd(b, a%b)
    
    return str1[:gcd(len(str1), len(str2))] if (str1 + str2 == str2 + str1) else ''
