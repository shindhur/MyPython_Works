list_1 = [i for i in range(1000000)]
list_2 = [j**2 for j in range(1000000)]

import time
import numpy as np

t0 = time.time()
product_list = list(map(lambda x, y: x*y, list_1, list_2))
t1 = time.time()
print(t1-t0)

array_1 = np.array(list_1)
array_2 = np.array(list_2)
t0 = time.time()
array_3 = array_1 * array_2
t1 = time.time()
print(t1-t0)

