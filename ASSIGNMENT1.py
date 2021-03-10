"""Q1"""
X=int(input("Enter first number"))
Y=int(input("Enter second number"))
a=X**Y
print(a)

"""OP:
   
Enter first number3

Enter second number2
9
"""

#Q2.
list=[1,2,3,4,5,6,7,8,9,12,15,17]
for i in list:
    if(i%3==0):
        print(i)
"""OP:
    3
    6
    9
   12
   15"""