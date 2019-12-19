import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

plt.figure('TES')

#plot ke-01
plt.subplot(322) #baris ada 1, kolom ada 2, di posisi ke-satu
plt.plot([1,2,3], [4,5,6])
plt.title('Tes 1')

#plot ke-02
plt.subplot(323)
plt.plot([1,2,3],[3,2,1])
plt.title('Tes 2')

plt.suptitle('Ini super title', size=20)
plt.show()


#FIGURE KE-02
plt.figure('CEK')

#plot ke-01
plt.subplot(322) #baris ada 1, kolom ada 2, di posisi ke-satu
plt.plot([1,2,3], [4,5,6])
plt.title('Tes 1')

#plot ke-02
plt.subplot(323)
plt.plot([1,2,3],[3,2,1])
plt.title('Tes 2')

plt.suptitle('Ini super title', size=20)
plt.show()