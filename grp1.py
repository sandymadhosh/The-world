import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(50, 80, 101)
y = np.exp(-x)*np.sin(np.pi*x)
plt.plot(x,y)
plt.title('First test of Spyder')
plt.savefig('tmp.png')
plt.show()


