import matplotlib.pyplot as plt

def polar_rz(inp):
    inp1=list(inp)
    inp1=[-1 if i==0 else 1 for i in inp1]
    li=[]
    for i in range(len(inp1)):
        li.append(inp1[i])
        li.append(0)
    return li

def plot(li):
    plt.ylabel("Polar-RZ")
    plt.plot(polar_rz(li),drawstyle='steps-pre')
    plt.show()

if __name__=='__main__':
    size= 6
    li=[0,0,1,1,0,1]
    plot(li)