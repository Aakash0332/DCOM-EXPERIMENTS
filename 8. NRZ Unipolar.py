import matplotlib.pyplot as plt

def unipolar(inp):
    inp1=list(inp)
    inp1.insert(0,0)
    return inp1

def plot(li):
    plt.ylabel("Unipolar-NRZ")
    plt.plot(unipolar(li),drawstyle='steps-pre')
    plt.show()

if __name__=='__main__':
    size= 6
    li=[0,0,1,1,0,1]
    plot(li)