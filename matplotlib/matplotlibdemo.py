#!/usr/bin/env python3

import matplotlib.pyplot as plt
from numpy.random import randn
fig=plt.figure(2)
ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
print(randn(50).cumsum())
plt.plot(randn(50).cumsum(),'k--')
plt.show()