a = []
n = int(input("Enter number of data bits : "))
for i in range(0, n):
    ele = int(input())
    a.append(ele)
print("Data bits",a)
b=a[0]^a[1]^a[2]^a[3]^a[4]^a[5]^a[6]^a[7]
print("Ex-or of data bits",b)
a.append(b)
print("Transmitter bits",a)
d = []
n = int(input("Enter number of Transmitted bits : "))
for i in range(0, n):
    ele = int(input())
    d.append(ele)
print("Received bits",d)
c=d[0]^d[1]^d[2]^d[3]^d[4]^d[5]^d[6]^d[7]^d[8]
print("Ex-or of Received bits",c)
if c == 0:
    del a[-1]
    print("No Error\n","Decoder Output",a)

else:
    print("Error No Decoding")