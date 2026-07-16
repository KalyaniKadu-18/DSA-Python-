def SumOfDigits():
    n = 123
    sum = 0
    while n>0:
          digit = n % 10
          sum += digit
          n //= 10
    return sum
print(SumOfDigits())