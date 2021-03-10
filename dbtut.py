# import math
# x=int(input("Enter the value of x in degrees:"))
# n=int(input("Enter the number of terms:"))
# sine = 0
# pi = 22/7
# for i in range(n):
#    sign = (-1)**i
#    y=x*(pi/180)
#    sine = sine + ((y**(2.0*i+1))/math.factorial(2*i+1))*sign
#
# print(sine)
#

row = 5
for k in range(row+1,1,-1):
    for j in range(k*2,1,-2):
        print(9-j, end=" ")
    print("")