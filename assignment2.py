
"""
@author: JoshuaDGonzalez
project:assignmnet two
"""

import numpy as np

a = np.random.rand(4,2)

print(a)

#loop  through the matrix two times, print one colum than the next
for i in range(2):
    for b in range(4):
        print(a[b][i])
