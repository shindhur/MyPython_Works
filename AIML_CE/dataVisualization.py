import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.linspace(5, 100, 100)
y = np.linspace(10, 1000, 100)

plt.plot(x, y)
plt.show()

plt.plot([1, 4, 6, 8], [3, 8, 3, 5], 'b', linestyle='dashdot')
plt.xlabel("Current")
plt.ylabel("Voltage")
plt.title("1st Data Visualization Plot")
plt.xlim([0, 20])
plt.ylim([0, 20])
plt.show()

#------------------------------------

x = np.linspace(1, 10, 100)
y = np.log(x)

plt.figure(1)

plt.subplot(121)
plt.title("y=log(x)")
plt.plot(x, y)

plt.subplot(122)
plt.title("y=log(x)**2")
plt.plot(x, y**2)

plt.show()
#------------------------------------