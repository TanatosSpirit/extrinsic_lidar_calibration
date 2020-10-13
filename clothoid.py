import numpy as np
from scipy.special import fresnel
import pylab


t = np.linspace(-6, 6, 100)
pylab.plot(*fresnel(t), c='k')
pylab.show()