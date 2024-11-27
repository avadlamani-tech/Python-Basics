import numpy as np
from matplotlib import pyplot as plt


x = np.arange(1,11)
y = 2 * x + 5
plt.title("Ashwin's Car Sales") 
plt.xlabel("Number of cars")
plt.ylabel("NUmber of days") 
plt.plot(x,y)
plt.show()