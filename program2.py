def Is2():
    a = int(input("Enter the first value: "))
    b = int(input("Enter another value: "))
    c = int(input("Enter the third value: "))
    
    if a > b and a > c:
        print(a, "is largest")
        
    elif b > c and b > a:
       print(b, "is largest")
       
    elif c > a and c > b :
       print(c, "is largest")
       
    else:
        print(a, "=", b, "=", c)


Is2()
