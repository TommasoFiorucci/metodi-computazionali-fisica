# esercizio 3 esercitazione 5

#Passo 1:

#Creare uno script python che esegua le seguenti operazioni:

# Legga uno o più file di input;

# Produca un istogramma dei tempi per uno dei moduli (file);

# Produca un istogramma delle differenze di tempi (delta_t)
# fra Hit consecutivi per uno dei moduli;
# SUGGERIMENTO: usare il Log(delta_t) (log in base 10)

# Interpretare il grafico risultante.

# leggo il file hit_times_M0.csv

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

tabella = pd.read_csv("hit_times_M0.csv")

print(tabella)

l = len(tabella["hit_time"])

tempi = np.zeros(l)

for i in range(l):
    tempi[i] = tabella["hit_time"][i]


# chiedo a python di disegnare l'istogramma

n, bis, p = plt.hist( tempi, bins = 100, range = (287827, 999309576))

plt.show()


#calcoliamo l'array delle differenze "a mano"
delta_t = np.empty(0)
for i in range(1, l):
    diff = tempi[i] - tempi[i - 1]
    delta_t = np.append(delta_t, diff)

print("tabella", delta_t)

# ordiniamo l'array delta_t
delta_t_ord = delta_t
a = 0
#for i in range(0, len(delta_t)):
#    for j in range(0, len(delta_t)):
#        a = delta_t_ord[i]
#        diff_t = delta_t_ord[i] - delta_t_ord[j]
#        if diff_t < 0:
#            delta_t[i] = delta_t_ord[j]
#            delta_t[j] = a


n, bis, p = plt.hist(delta_t, bins = 1000, range = (0, len(delta_t)))

plt.show()

x = np.arange(len(delta_t))
plt.plot(x, delta_t)

plt.show()
