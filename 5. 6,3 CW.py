c1=[1,0,0,1,1,0]
c2=[0,1,0,0,1,1]
c3=[0,0,1,1,0,1]
print("The given matrix is :\n",'\n',c1,'\n',c2,'\n',c3)
print("\n\nTHE LINEAR BLOCK CODE IS :")
print("\n000 ---> [0, 0, 0, 0, 0, 0]\n001 --->",c3,"\n010 --->",c2)
a = [c2[0]^c3[0],c2[1]^c3[1],c2[2]^c3[2],c2[3]^c3[3],c2[4]^c3[4],c2[5]^c3[5]]
print("011 --->",a)
print("100 --->",c1)
b = [c1[0]^c3[0],c1[1]^c3[1],c1[2]^c3[2],c1[3]^c3[3],c1[4]^c3[4],c1[5]^c3[5]]
print("101 --->",b)
c = [c1[0]^c3[0],c1[1]^c3[1],c1[2]^c3[2],c1[3]^c3[3],c1[4]^c3[4],c1[5]^c3[5]]
print("110 --->",c)
d = [c1[0]^c2[0]^c3[0],c1[1]^c2[1]^c3[1],c1[2]^c2[2]^c3[2],c1[3]^c2[3]^c3[3],c1[4]^c2[4]^c3[4],c1[5]^c2[5]^c3[5]]
print("111 --->",d)
Hd=3
print("\nThe minimum hamming distance is: ", Hd)
Dc=Hd-1
print("\nThe detection capability is: ", Dc)
Cc=(Hd-1)/2
print("\nThe correction capability is: ", Cc)