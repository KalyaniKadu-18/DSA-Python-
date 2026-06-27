n = int(input("Enter a num: "))
leftover = 0
max_size = 0

for _ in range(n):
    packet = int(input("Enter package size: "))
    total = leftover + packet

    power = 1
    while power * 2 <= total:
        power *= 2

    if power >= max_size:
        max_size = power

    leftover = total - power

print(max_size)