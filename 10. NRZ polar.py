import matplotlib.pyplot as plt

def polar_nrz_l(inp):
    inp1=list(inp)
    inp1.insert(0,0)
    inp1=[-1 if i==0 else 1 for i in inp1]
    return inp1

def plot(li):
    plt.ylabel("P-NRZ-L")
    plt.plot(polar_nrz_l(li),drawstyle='steps-pre')
    plt.show()
    
if __name__=='__main__':
    size= 6
    li=[0,0,1,1,0,1]
    plot(li)