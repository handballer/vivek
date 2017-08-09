num=int(input("enter the year"))
if(num%4)==0&(num%100)==0 &(num%400)==0:
    print ("it is a leap year")
else:
    print ("it is not a leap year")
