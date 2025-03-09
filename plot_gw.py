import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from numpy import log10 as lg
from numpy import pi as pi
from scipy.interpolate import interp1d as sp_interp1d
from scipy.interpolate import splrep,splev
from scipy.integrate import odeint
from scipy.integrate import ode
import warnings
import timeit
import scipy.optimize as opt
from matplotlib import cm
from astropy import constants as const
from astropy import units as u
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset


import matplotlib.font_manager as font_manager

plt.rcParams['xtick.labelsize'] = 30
plt.rcParams['ytick.labelsize'] = 30
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.major.size'] = 8
plt.rcParams['ytick.major.size'] = 8
plt.rcParams['xtick.minor.size'] = 4
plt.rcParams['ytick.minor.size'] = 4
plt.rcParams['xtick.top'] = True
plt.rcParams['ytick.right'] = True
plt.rcParams['axes.labelpad'] = 8.0
plt.rcParams['figure.constrained_layout.h_pad'] = 0
plt.rcParams['text.usetex'] = True
plt.rc('text', usetex=True)
plt.tick_params(axis='both', which='minor', labelsize=18)
import matplotlib.ticker
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)



data1 = np.genfromtxt('data_gw.dat')
c0, c1, c2= data1[:, 0], data1[:, 1], data1[:, 2]
Ntrim1 = 16670
c01=c0[:Ntrim1]
c11=c1[:Ntrim1]
c21=c2[:Ntrim1]



fig, (ax1,ax2) = plt.subplots(2, 1,figsize=(24,10),sharex=True, sharey=False)
plt.subplots_adjust(hspace=0.0)

ax1.set_ylabel(r'$ rh_+ \,[t_c] $', fontsize=30)
ax2.set_ylabel(r'$ rh_\times \,[t_c] $', fontsize=30)
ax2.set_xlabel(r'$t \,[t_c]$', fontsize=40)
    
ax1.plot(c01, c11)
ax2.plot(c01, c21)
#ax1.plot(c01, c21, linestyle='--', color = 'gray')

#ax2.plot(d01, d21, linestyle='--', color = 'gray')

ax2.set_xlim(c01[0], c01[-1])
ax1.minorticks_on()
ax2.minorticks_on()

#ax1.legend(loc='best', fontsize=30)




plt.savefig("plot_gw.pdf", format='pdf', bbox_inches="tight")

#plt.show()
