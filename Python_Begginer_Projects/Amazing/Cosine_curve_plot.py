import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0,2.0,0.01)
s = 1 + np.cos(2*np.pi*t)

plt.grid()
plt.plot(t,s, '--')
plt.xlabel('Time (t)')
plt.ylabel('Voltage (v)')
plt.title('Cosine Curved plot')
plt.show()