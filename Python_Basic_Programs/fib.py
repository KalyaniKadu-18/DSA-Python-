def Fib():
    a = 0
    b = 1
    n = 10
    for i in range(n):
        print(a , end=" ")
        c = a + b
        a = b
        b = c
Fib()
       
    