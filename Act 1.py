try:
    n=int(input("Enter the number:"))
    print("the number entered is",n)

except ValueError as e:
    print("Exeption as",e)