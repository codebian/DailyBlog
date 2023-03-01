
import numpy as np
import matplotlib.pyplot as plt
import sys

file1=sys.argv[1]
tmpp=np.genfromtxt("%s"%file1,skip_header=24)
plt.plot(tmpp[:,0],tmpp[:,1])
plt.show()
