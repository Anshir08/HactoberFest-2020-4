a, b, c = float(input("Enter the coefficient a")), float(input("Enter the coefficient b")), float(input("Enter the coefficient c"))

d = (b**2) - (4*a*c)
if d>0:
    r1=(-b + d**(1/2))/(2*a)
    r2 =(-b - d**(1/2))/(2*a)
    print("Roots are real and unequal",r1,"and",r2)
elif d==0:
    r1=-b/(2*a)
    print("Roots are real and same",r1)
else:
    print("No real roots are there")
