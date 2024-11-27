import numpy as np
import matplotlib.pyplot as plt

#Compute the x and y coordinates for points
x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)
plt.title("Sine wave form")
 #plot the point using matplotlib
plt.plot(x,y)
plt.show()