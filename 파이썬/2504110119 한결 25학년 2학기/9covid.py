import numpy as np
import matplotlib.pyplot as plt

months=np.arange(1,13)
num_cases=[11,2920,6636,750,615,1141,1044,5473,3707,2444,7324,26198]
cum_cases=np.cumsum(num_cases)

plt.figure(figsize=(5,3))
plt.plot(months,num_cases,label='number of cases')
plt.plot(months,cum_cases,label='accumulated number of cases')
plt.xlabel('months')
plt.legend()
plt.show()