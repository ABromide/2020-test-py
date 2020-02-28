import random
import os 
t=-1
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
      i=i-1
os.system("pause")
