num = int(input("enter a number: "))
num = str(num)
revnum = num[::-1]
if num == revnum:
    print("this number is palindrome")
else:
    print("you are a normal human")
