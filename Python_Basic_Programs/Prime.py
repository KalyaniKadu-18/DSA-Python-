def Prime():
    n = 8
    if n <= 1:
       print("Num is not prime nor composite")
       return
    for i in range(2 , n ):
        if n % i == 0:
           print("Num is not prime")
           return
    print("Num is prime")
Prime()
       
       