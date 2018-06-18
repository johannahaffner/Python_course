import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


measured_ccm = [1500, 1234, 1432, 1324, 1543]
simulated_ccm = [1600, 1114, 1632, 1111, 2333]

measured_cb = [200, 500, 333, 444]
simulated_cb = [188, 100, 123, 444]

fig = plt.figure()
plt.plot([0, 2500], [0, 2500], label='Linear Regression', color='k', alpha=0.3, linewidth=2)
plt.scatter(measured_ccm, simulated_ccm, label='Central Carbon Metabolism', color='r')
plt.annotate('important enzyme',
			 xy=(1234, 1111),
			 xytext=(1400, 500),
			 arrowprops=dict(facecolor='black', width=1, headwidth=7))
plt.scatter(measured_cb, simulated_cb, label='Cofactor Biosynthesis', color='b', s=500)
plt.text(1400, 200, "Hello.")
plt.xlim(0, 2000)
plt.ylim(0, 2000)
plt.legend()
plt.xlabel('Measured Protein Abundance [copies/cell]')
plt.ylabel('Simulated Protein Abundance [copies/cell]')
plt.show()

