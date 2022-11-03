import matplotlib.pyplot as plt

def AMI(inp):
    inp1=list(inp)
    inp1.insert(0,0)
    lock=False
    for i in range(len(inp1)):
        if inp1[i]==1 and not lock:
            lock=True
            continue
        elif lock and inp1[i]==1:
            inp1[i]=-1
            lock=False
    return inp1

def plot(li):
    plt.ylabel("A-M-I")
    plt.plot(AMI(li),drawstyle='steps-pre')
    plt.show()

if __name__=='__main__':
    size= 6
    li=[0,0,1,1,0,1]
    plot(li)