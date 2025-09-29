import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6,4))

for i in range(3):
    coin=np.random.randint(0,2,size=5000)
    ind=np.arange(1,len(coin)+1)
    p_c=np.cumsum(coin)/ind*100
    plt.plot(ind,p_c)
plt.ylim(0,100)
plt.ylabel('%')
plt.show()
