import math
px1 = 1/2
px2 = 1/4
px3 = 1/8
px4 = 1/8
rs = 1000

ix1 = math.log(1/px1,2)
ix2 = math.log(1/px2,2)
ix3 = math.log(1/px3,2)
ix4 = math.log(1/px4,2)

print ("Self informantion I(X1) = ",ix1)
print ("Self informantion I(X2) = ",ix2)
print ("Self informantion I(X3) = ",ix3)
print ("Self informantion I(X4) = ",ix4)

hx = (px1*ix1)+(px2*ix2)+(px3*ix3)+(px4*ix4)
print("Source entropy H(x) = ",hx)

R = hx*rs
print ("Average Information Ratio R = ",R)