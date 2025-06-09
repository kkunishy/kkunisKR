import matplotlib.pyplot as plt

name =['Jessica', 'Liam', 'Sophia']

x = [75, 92, 83]
y = [79, 89, 90]
plt.figure(figsize=(5,3))
plt.scatter(x, y)
plt.annotate(name[0],(x[0], y[0]), xytext=(5,-10),textcoords='offset points')
plt.annotate(name[1],(x[1], y[1]), xytext=(5,-10),textcoords='offset points')
plt.annotate(name[2],(x[2], y[2]), xytext=(5,-10),textcoords='offset points')
plt.xlim(73, 95)
plt.ylim(75, 93)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()