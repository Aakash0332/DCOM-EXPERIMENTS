print("(7,4) Hamming Code,error detection and correction")
print("The Generator Matrix (G) is:")
g1=[1,0,0,0,1,1,0]
g2=[0,1,0,0,0,1,1]
g3=[0,0,1,0,1,1,1]
g4=[0,0,0,1,1,0,1]
print('\n',g1,'\n',g2,'\n',g3,'\n',g4)
print("\n H Transpose of (G) is:")
h1=[g1[4],g1[5],g1[6]]
h2=[g2[4],g2[5],g2[6]]
h3=[g3[4],g3[5],g3[6]]
h4=[g4[4],g4[5],g4[6]]
h5=[g1[0],g1[1],g1[2]]
h6=[g2[0],g2[1],g2[2]]
h7=[g3[0],g3[1],g3[2]]
print('\n',h1,'\n',h2,'\n',h3,'\n',h4,'\n',h5,'\n',h6,'\n',h7)
R=input('Enter the receiver code: ')
Rx = [int(x) for x in str(R)]

R1=[Rx[0]*h1[0],Rx[0]*h1[1],Rx[0]*h1[2]]
R2=[Rx[1]*h2[0],Rx[1]*h2[1],Rx[1]*h2[2]]
R3=[Rx[2]*h3[0],Rx[2]*h3[1],Rx[2]*h3[2]]
R4=[Rx[3]*h4[0],Rx[3]*h4[1],Rx[3]*h4[2]]
R5=[Rx[4]*h5[0],Rx[4]*h5[1],Rx[4]*h5[2]]
R6=[Rx[5]*h6[0],Rx[5]*h6[1],Rx[5]*h6[2]]
R7=[Rx[6]*h7[0],Rx[6]*h7[1],Rx[6]*h7[2]]


RX1=(R1[0]^R2[0])^(R3[0]^R4[0])^(R5[0]^R6[0])^R7[0]
RX2=(R1[1]^R2[1])^(R3[1]^R4[1])^(R5[1]^R6[1])^R7[1]
RX3=(R1[2]^R2[2])^(R3[2]^R4[2])^(R5[2]^R6[2])^R7[2]
c=(RX1,RX2,RX3)
print("syndrome= ",RX1,RX2,RX3)
if c==(0,0,0):
    print("no error")
    print("correct codeword is: ",R)
elif c==(1,1,0):
    print("Error exists")
    e=[1,0,0,0,0,0,0]
    d=[Rx[0],Rx[1],Rx[2],Rx[3],Rx[4],Rx[5],Rx[6]]
    f=e[0]^d[0],e[1]^d[1],e[2]^d[2],e[3]^d[3],e[4]^d[4],e[5]^d[5],e[6]^d[6]
    print("correct codeword is: ",f)
elif c==(0,1,1):
    print("Error exists")
    e=[0,1,0,0,0,0,0]
    d=[Rx[0],Rx[1],Rx[2],Rx[3],Rx[4],Rx[5],Rx[6]]
    f=e[0]^d[0],e[1]^d[1],e[2]^d[2],e[3]^d[3],e[4]^d[4],e[5]^d[5],e[6]^d[6]
    print("correct codeword is: ",f)
elif c==(1,1,1):
    print("Error exists")
    e=[0,0,1,0,0,0,0]
    d=[Rx[0],Rx[1],Rx[2],Rx[3],Rx[4],Rx[5],Rx[6]]
    f=e[0]^d[0],e[1]^d[1],e[2]^d[2],e[3]^d[3],e[4]^d[4],e[5]^d[5],e[6]^d[6]
    print("correct codeword is: ",f)
elif c==(1,0,1):
    print("Error exists")
    e=[0,0,0,1,0,0,0]
    d=[Rx[0],Rx[1],Rx[2],Rx[3],Rx[4],Rx[5],Rx[6]]
    f=e[0]^d[0],e[1]^d[1],e[2]^d[2],e[3]^d[3],e[4]^d[4],e[5]^d[5],e[6]^d[6]
    print("correct codeword is: ",f)
elif c==(1,0,0):
    print("Error exists")
    e=[0,0,0,0,1,0,0]
    d=[Rx[0],Rx[1],Rx[2],Rx[3],Rx[4],Rx[5],Rx[6]]
    f=e[0]^d[0],e[1]^d[1],e[2]^d[2],e[3]^d[3],e[4]^d[4],e[5]^d[5],e[6]^d[6]
    print("correct codeword is: ",f)
elif c==(0,1,0):
    print("Error exists")
    e=[0,0,0,0,0,1,0]
    d=[Rx[0],Rx[1],Rx[2],Rx[3],Rx[4],Rx[5],Rx[6]]
    f=e[0]^d[0],e[1]^d[1],e[2]^d[2],e[3]^d[3],e[4]^d[4],e[5]^d[5],e[6]^d[6]
    print("correct codeword is: ",f)
elif c==(0,0,1):
    print("Error exists")
    e=[0,0,0,0,0,0,1]
    d=[Rx[0],Rx[1],Rx[2],Rx[3],Rx[4],Rx[5],Rx[6]]
    f=e[0]^d[0],e[1]^d[1],e[2]^d[2],e[3]^d[3],e[4]^d[4],e[5]^d[5],e[6]^d[6]
    print("correct codeword is: ",f)
else:
    print("itna galat kaise ho skta h bhai??")