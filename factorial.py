def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
try:
    n=int(input("Enter a non negative integre"))
    if n<0:
        print("Factorial is not define for negative number")
    else:
        f=fact(int(n))
        print(f"The factorila  of {n} is {f}")
except ValueError:
    print("Invalid  intput. Please enter a non-negative number")