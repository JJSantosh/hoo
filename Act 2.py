try:
    n1=int(input("Enter the n1:"))
    n2=int(input("Enter the n2:"))
    result=n1/n2
    print("result:",result)
    print("result1:",result1)

except ValueError:
    print("pls enter the numbers only")

except ZeroDivisionError:
    print("do not divide the number by zero")

except NameError:
    print("pls do not enter names")

except SyntaxError as e:
    print("Exception",e)

finally:
    print("Finally executed")