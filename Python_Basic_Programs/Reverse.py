def Reverse():
    n = 123
    reverse = 0
    while n > 0:
          digit = n % 10
          reverse = reverse * 10 + digit
          n //= 10
    return reverse
print(Reverse())