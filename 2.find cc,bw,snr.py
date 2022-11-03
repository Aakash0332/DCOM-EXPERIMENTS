import math
print("Enter 1 for Gaussian Channel Capacity\nEnter 2 for BandWidth\nEnter 3 for SNR")
a = int(input("Enter Number :"))
if a == 1:
  B = float(input("Enter BandWidth :"))
  S = float(input("Enter SNR :"))
  C = B*math.log(1+S,2)
  print ("Gaussian Channel Capacity :",C)
elif a == 2:
  C = float(input("Enter Capacity :"))
  S = float(input("Enter SNR :"))
  B = C/math.log(1+S,2)
  print ("BandWidth :",B)
elif a == 3:
  B = float(input("Enter BandWidth :"))
  C = float(input("Enter Capacity :"))
  S = 2**(C/B)-1
  print ("SNR :",S)
else:  print("Enter Correct Number")