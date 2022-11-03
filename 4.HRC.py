a = []
n = int(input("Enter number of data bits : "))
for i in range(0, n):
    ele = int(input())
    a.append(ele)

print("Data bits :",a)
b = [a[0],a[1],a[2],a[3]]
c = [a[4],a[5],a[6],a[7]]
print("Charater bits :",b,c)

d=[b[0]^c[0],b[1]^c[1],b[2]^c[2],b[3]^c[3]]
print("HRC Character bits Ex-or :",d)
e = a+d
print("Transmitted bits :",e)

f = []
n = int(input("Enter number of Transmitter bits : "))
for i in range(0, n):
    ele = int(input())
    f.append(ele)

g = [f[0],f[1],f[2],f[3]]
h = [f[4],f[5],f[6],f[7]]
j = [f[8],f[9],f[10],f[11]]
print("Received Character bits :",g,h,j)
k = [g[0]^h[0]^j[0],g[1]^h[1]^j[1],g[2]^h[2]^j[2],g[3]^h[3]^j[3]]
print("HRC Received Character bits Ex-or :",k)
l=1
if l in k:
    print("Error NO Decoding")
else:
    print("No Error","\nDecoder Output:",a)
