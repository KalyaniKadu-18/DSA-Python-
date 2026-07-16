def NoDivides(num: int) -> int:
    temp = num
    result = 0
    while temp>0:
         r = num % 10
         if r % 10 == 0:
            result += 1
         temp//=10

         return result
print(NoDivides(10))
