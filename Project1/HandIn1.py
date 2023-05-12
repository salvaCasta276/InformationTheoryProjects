import numpy as np

class InfoTheory:

    def Entropy(self, p):
        if p.ndim != 2:
            raise Exception("Input should be a numpy array with shape (n, m)")
        
        if p.shape[1] == 1:
            p = np.concatenate((p, 1-p), 1)

        return -(p*np.log2(p, where=p!=0)).sum(axis = 1)

    def MutualInformation(self, p):
        if p.ndim != 2:
            raise Exception("Input should be a numpy array with shape (n, m)")

        p_x = np.sum(p, 1)
        p_y = np.sum(p, 0)

        sum = 0
        for x, y in np.ndindex(np.shape(p)):
            if p[x,y]!=0:
                sum += p[x,y] * np.log2(p[x,y] / ( p_x[x] * p_y[y]))

        return np.array([sum])


if __name__ == '__main__':

    ### init
    IT = InfoTheory()

    ### 1st test
    P1 = np.transpose(np.array([np.arange(0.0,1.1,0.25)]))
    print(P1)
    H1 = IT.Entropy(P1)
    print("H1 =",H1)

    ### 2nd test
    P2 = np.array([
        [0.3, 0.1, 0.3, 0.3],
        [0.4, 0.3, 0.2, 0.1],
        [0.8, 0.0, 0.2, 0.0]
    ])
    H2 = IT.Entropy(P2)
    print("H2 =",H2)

    ### 3rd test
    P3 = np.array([
        [0, 3/4],
        [1/8, 1/8]
    ])
    I1 = IT.MutualInformation(P3)
    print("I1 =",I1)

    ### 4th test
    P4 = np.array([
        [1/12, 1/6, 1/3],
        [1/4, 0, 1/6]
    ])
    I2 = IT.MutualInformation(P4)
    print("I2 =",I2)

    ### 5th test --- Independent variables
    p = [1/2, 1/3, 1/6, 0]
    q = [1/7, 3/7, 2/7, 1/7]
    r = np.zeros((4,4))
    for x, y in np.ndindex(np.shape(r)):
        r[x,y] = p[x] * q[y]
    I3 = IT.MutualInformation(r)
    print("I3 =", I3)
