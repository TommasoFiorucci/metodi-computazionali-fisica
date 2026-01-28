import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import reco


tab0 = pd.read_csv('hit_times_M0.csv')
tab1 = pd.read_csv('hit_times_M1.csv')
tab2 = pd.read_csv('hit_times_M2.csv')
tab3 = pd.read_csv('hit_times_M3.csv')

print(tab0)

l0 = len(tab0['hit_time'])
l1 = len(tab1['hit_time'])
l2 = len(tab2['hit_time'])
l3 = len(tab3['hit_time'])

"""scriviamo un array che contiene tutti gli elementi reco.Hit() del file"""

eventi_0 = np.empty(0)
for i in range(l0):
    ev = reco.Hit()
    ev.riv(tab0['mod_id'][i], tab0['det_id'][i], tab0['hit_time'][i])
    eventi_0 = np.append(eventi_0, ev)

eventi_1 = np.empty(0)
for i in range(l1):
    ev = reco.Hit()
    ev.riv(tab1['mod_id'][i], tab1['det_id'][i], tab1['hit_time'][i])
    eventi_1 = np.append(eventi_1, ev)

eventi_2 = np.empty(0)
for i in range(l2):
    ev = reco.Hit()
    ev.riv(tab2['mod_id'][i], tab2['det_id'][i], tab2['hit_time'][i])
    eventi_2 = np.append(eventi_2, ev)

eventi_3 = np.empty(0)
for i in range(l3):
    ev = reco.Hit()
    ev.riv(tab3['mod_id'][i], tab3['det_id'][i], tab3['hit_time'][i])
    eventi_3 = np.append(eventi_3, ev)

eventi = np.concatenate((eventi_0, eventi_1, eventi_2, eventi_3))
l = len(eventi)
print(len(eventi))

"""ordiniamo tutti gli elementi reco.Hit()
in base al loro timestamp"""

print(eventi[0] < eventi[1])
ev_or = np.sort(eventi)

"""creiamo un array che contiene tutte le differenze temporali tra un
elemento di eventi e quello immediatamente precedente"""

ev_delta = np.empty(0)
for i in range(l - 1):
    delta = ev_or[i + 1] - ev_or[i]
    ev_delta = np.append(ev_delta, delta)

print(ev_delta)
print(len(ev_delta))

"""rappresentiamo le differenze temporali con un istogramma"""

dtmask = ev_delta > 0
plt.hist(ev_delta[dtmask], bins = 2000, range = (100, len(ev_delta)))
#plt.yscale('log')
plt.show()
            
