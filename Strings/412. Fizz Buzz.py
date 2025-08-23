#
def fizzBuzz(self, n: int) -> List[str]:
    l=[]
    for i in range (1,n+1):
        if i%3==0:
            if i%5==0:
                l.append("FizzBuzz")
                continue
            else:
                l.append("Fizz")
                continue
        if i%5==0:
            l.append("Buzz")
            continue
        l.append(str(i))
    return l
        
