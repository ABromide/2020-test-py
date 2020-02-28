def decimalTOHEX(decimalNUMBER):
    leaveNUMBER=''
    while decimalNUMBER!=0:
       midNUNBER=int(decimalNUMBER%16) 
       if  midNUNBER>=10 :
           midNUNBER=chr(midNUNBER-10+ord("A"))
       else:
           midNUNBER=chr(midNUNBER+ord('0'))
       leaveNUMBER=midNUNBER+leaveNUMBER
       decimalNUMBER=decimalNUMBER//16

    return leaveNUMBER

""" def main(): """
number=eval(input("Please input a decimal number!\n"))
print("Decimal number : ",number,"\nHex number : ",decimalTOHEX(number))
import os 
os.system("pause")
    
       