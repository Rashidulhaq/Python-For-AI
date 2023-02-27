import numpy as np
f = np.array([[0,0], [1,0], [0,1], [1,1]])
label = np.array([0,1,1,1])

w = [1,0.5]
theta = 0.5
learning = 0.1
n= -1
epoch = 5
for j in range (0, epoch):
    for i in range (0, f.shape[0]):
        actual = label [i]
        instant = f[i]
        x1 = instant[0]
        x2 = instant[1]
        net = w[0]*x1+w[1]*x2-theta
        
        if net>0:
            y=1
        else:
            y=0
            
        delta = actual - y
        
        if delta != 0:
            w[0] = w[0]+learning * delta *x1
            w[1] = w[1]+learning * delta *x2
            theta = n*learning * delta + theta
            
        print("calculate value",y, "actual value",delta)
        
    print("-----------------------------------")
