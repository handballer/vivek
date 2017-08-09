num1= int(input ("enter the first number: "))
num2= int(input ("enter the second number: "))
num3= int(input("enter the third number: "))
num4= int(input("enter the fourth number: "))
num5= int(input("enter the fifth number: "))
if ((num1<num2)&(num1<num3)&(num1<num4)&(num1<num5)):
    print ("num1 is smallest")
elif((num2<num3)&(num2<num1)&(num2<num4)&(num2<num5)):
    print ("num2 is smallest")
elif((num3<num1)&(num3<num2)&(num3<num4)&(num3<num5)):
    print("num3 is smallest")
elif((num4<num1)&(num4<num2)&(num4<num3)&(num4<num5)):
    print("num4 is smallest")
else :
    print("num5 is smallest",num5)

