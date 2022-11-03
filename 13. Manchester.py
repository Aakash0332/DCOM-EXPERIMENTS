import matplotlib.pyplot as plt

def manchester(inp):
    inp1=list(inp)
    li,init=[],False
    for i in range(len(inp1)):
        if inp1[i]==0:
            li.append(-1)
            if not init:
                li.append(-1)
                init=True
            li.append(1)
        elif inp1[i]==1 :
            li.append(1)
            li.append(-1)
    return li

def plot(li):
    plt.ylabel("Manchester")
    plt.plot(manchester(li),drawstyle='steps-pre',marker='>')
    plt.show()

if __name__=='__main__':
    size= 6
    li=[0,0,1,1,0,1]
    plot(li)