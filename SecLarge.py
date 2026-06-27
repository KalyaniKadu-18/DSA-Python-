n = int(input("Enter a num:"))
arr = []

for i in range(n):
    arr.append(int(input("Enter a num: ")))

arr = list(set(arr))
arr.sort()

if len(arr) < 2:
    print("No second largest element")
else:
    print("second largest is:",arr[-2])    
