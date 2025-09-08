import numpy as np
import matplotlib.pyplot as plt

year=[2017,2018,2019,2020,2021]
spring=np.array([124.9,383.5,175.0,173.7,330.5])
summer=np.array([124.9,383.5,175.0,173.7,330.5])
fall=np.array([124.9,383.5,175.0,173.7,330.5])
winter=np.array([124.9,383.5,175.0,173.7,330.5])

plt.figure(figsize=(6,4))
plt.plot(year,spring,label='spring')
plt.plot(year,summer,label='summer')
plt.plot(year,fall,label='fall')
plt.plot(year,winter,label='winter')
plt.ylim(100,400)
plt.legend()
plt.show()