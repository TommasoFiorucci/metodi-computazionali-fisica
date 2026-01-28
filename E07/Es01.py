# esercizio 1 esercitazione 7

# leggo il file csv relativo all'esperimento e chiedo a python di scrivere
# una tabella contenente i dati dell'esperimento

import pandas as pd
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt


tabella = pd.read_csv("http://opendata.cern.ch/record/5203/files/Jpsimumu.csv")

print(tabella)

# calcolo la massa invariante della particella madre per ognuno dei 20000 eventi

s = tabella.shape

E1 = tabella["E1"]
E2 = tabella["E2"]
px1 = tabella["px1"]
py1 = tabella["py1"]
pz1 = tabella["pz1"]
px2 = tabella["px2"]
py2 = tabella["py2"]
pz2 = tabella["pz2"]

c = sp.constants.c

m = np.zeros(s[0])
for i in range(s[0]):
    m[i] = (1 / c**2) * ( (E1[i] + E2[i])**2 + (px1[i] + px2[i])**2 + (py1[i] + py2[i])**2 + (pz1[i] + pz2[i])**2 )**(1/2)

print(m)

# chiedo a python di disegnare un istogramma della massa invariante calcolata

mm = np.random.normal(100, 20, 500)

n = plt.hist(m, bins = 50, range = (0, 30 * 10**(-16)))
plt.ylabel("EVENTI")
plt.xlabel("MASSA INVARIANTE")

plt.show()

# chiedo a python di disegnare un istogramma attorno al picco dell'istogramma precedente

plt.hist(m, bins = 100, range = (0, 7 * 10**(-16)))
plt.ylabel("EVENTI")
plt.xlabel("MASSA INVARIANTE")

plt.show()

# provo ad eseguire il fit dei dati attorno al picco principale con la funzione f_g1


# cerco il picco dei dati, cioè dell'istogramma
# possibilmente senza usare cicli for

l_bin = 30 * 10**(-16) / 50
bins = np.arange(0, 30 * 10**(-16), l_bin)

m_p = (bins[5] - bins[4]) / 2 #picco dell'istogramma

# definisco la funzione gaussiana + polinomio di primo grado f_g1(x)

def fg1(x, a, sig, p1, p0):

    f_g1 = a * np.ex(-(x - m_p)**2 / (2 * sig**2)) + p1 * x + p0

    return f_g1

# voglio usare il modulo curve_fit del modulo ptimize di scipy
# cioè optimize.curve_fit
# per fare ciò ho bisogno di una funzione e di due set di dati,
# uno per l'asse x e uno per l'asse y
# ho già definito la funzione
# devo definire le coordinate sul piano cartesiano
# dei dati di cui va fatto il fit

m_b = bins
n_e = np.zeros(len(bins)) # numero eventi
for i in range(len(bins)):
    n_e[i] = n[0][i]





print(bins)

print(tabella.columns)
