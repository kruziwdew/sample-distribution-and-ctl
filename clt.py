import numpy as np 
import matplotlib.pyplot as plt 

num = [1,10,50,100]
nummeans = []

for j in num:
    np.random.seed(1)
    x = [np.mean(np.random.randint(-40,40,j)) for _i in range (1000)]
    nummeans.append(x)
    
k = 0 

figure, ax = plt.subplots(2,2, figsize = (6,6))
for i in range (0,2):
    for j in range(0,2):
        ax [ i,j].hist(nummeans [ k ],10,density=True)
        k = k+1
plt.show()