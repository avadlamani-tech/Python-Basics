import numpy as np
import matplotlib.pyplot as plt

#Compute the x and y coordinates for points on sine and cosien curves
x = np.arange(0,3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

#Set up a subplot grid that has height and 2 and witdth 1,
#and set the first such ubplot as active
plt.subplot(2, 1, 1)

#make the first plot
plt.plot(x, y_sin)
plt.plot('sine')

#set the second subplot as active, and make the second plot
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('cosine')
plt.show()