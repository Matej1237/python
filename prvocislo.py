for a in range(1,100):
    x = 0
    b = 2
    while b < a:
        if a % b == 0:
            x = 1
            b = b + 1
        else:
            b = b + 1

    if x == 0:
        print (str(a) + ' je prvocislo')
    else:
        x = 0
