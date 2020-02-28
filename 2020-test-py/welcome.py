""" """ """ """ """
print("welcome to py")
print("awdioj")
print("dkajwndkl")
print(123 / 12)
import turtle
turtle.showturtle()
turtle.goto(0,20)
turtle.done()
""" """


import turtle
#输入两点的xy
x1=eval(input("please input the x of the frist number"))
y1=eval(input("please input the y of the frist number"))
x2=eval(input("please input the x of the second number"))
y2=eval(input("please input the y of the second number"))

distant=int(((x1-x2)**2+(y1-y2)**2)**0.5*100)/100.0
print(distant)

import turtle
turtle.showturtle()
turtle.penup()
turtle.goto(x1,y1)
turtle.write(x1,y1)
turtle.pendown()
turtle.goto(x2,y2)
turtle.write(x2,y2)
turtle.penup()
turtle.goto((x1+x2)/2,(y1+y2)/2)
turtle.write(distant)
turtle.penup()
turtle.done() """ """ """

""" import math
b=math.radians(90)
a=math.sin(b)

print(a) """

""" s1=input("wadwd")
print("s1 is "+ s1) """

""" s="\nawejoij\n"
s2=s.lower()
print(s2)

a=input("leaea\n").upper()
print(a)
a2=213
print(format(a2,"10b")) """

""" print(bool(1.2))

import random
a=random.randint(1,10)
b=random.randint(1,10)

print("what is",a,"+",b,"?")
c=eval(input())
if c==a+b:
  print("you are right !")
else:
  print("fuck bitch") 
 """
""" imcome=1131
if imcome<10000:
    tax=round(imcome * 0.1)
elif imcome<=20000:
    tax=10000 * 0.1 +(imcome-10000)*0.2

print(tax)
 """

""" if -2+x>23 :
  print(2)
else:
  print(3) """
""" a=0
sum=0
for a in range(100):
  sum+=1
print (round(sum)) """

import random


""" t=-1
fristnumber=random.randint(0,100)
secondnumber=random.randint(0,100)
print(fristnumber,secondnumber)
i=min(fristnumber,secondnumber)
while t!=1:
    if fristnumber%i==0 and secondnumber%i==0:
      print(i) 
      print("\n")
      t=1
    else:
      i=i-1 """

