import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import rivelatore as rv

#simuliamo un evento nella MWPC

d = 1
n_p = 5
su = 10**(-4)
sf = 5*10**(-5)
nr = 10**4
tc = 10**(-12)

#'generiamo' il rivelatore
a = rv.rivelatore(d, n_p, su, sf, nr, tc)

#simuliamo il passaggio della carica
p = a.passaggio(d, n_p)
print(p)

#simuliamo la diffusione
dif = a.diffusione(d, su, sf, p[1], nr)

#contiamo gli elettroni rivelati
eriv = dif[2]
print('Il numero di elettroni che sono stati rivelati è: ', len(eriv))

#calcoliamo il tempo di deriva degli elettroni che sono stati rivelati
t = np.empty(0)
for i in eriv:
    t_d = a.tempo(tc, len(eriv[i]))
    t = np.append(t, t_d)

print('i tempi di deriva degli elettroni rivelati sono: ', t)
print(len(t))

#calcoliamo il tempo di deriva minimo
#organizziamo l'array temporale in ordine decrescente

b = 0
for i in range(len(t)):
    for j in range(i, len(t)):
        dt = t[i] - t[j]
        if dt < 0:
            b = t[i]
            t[i] = t[j]
            t[j] = b
print(t)
tmax = t[0]
tmin = t[-1]
tav = np.sum(t)/len(t)

print('Il tempo di deriva massimo è: ', tmax)
print('Il tempo di deriva minimo è: ', tmin)
print('Il tempo di deriva medio è: ', tav)
