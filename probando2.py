


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


plt.figure(figsize=(8, 8))
m = Basemap(projection='ortho', resolution=None)
m.bluemarble(scale=0.5)




plt.savefig('probando2 Map')