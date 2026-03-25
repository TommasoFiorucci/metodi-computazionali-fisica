import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd

#leggiamo i dati del documento

tab = pd.read_csv('copernicus_PG_selected.csv')

print(tab)
print(tab.shape)
print(tab.columns)

#per rappresentare il tempo scegliamo la colonna tab['date'] della tabella
#invece che tab['date_old']

t = np.array(tab['date'])

#creiamo un dizionario contenente tutti gli array relativi sgli inquinanti
#atmosferici. Questo ci aiuterà a manipolare i dati più facilmente in futuro
#per esempio usando un ciclo for

inq = {}
for i in range(2, tab.shape[1]):
    inq.update({i-2 : np.array(tab[tab.columns[i]])})

#disegnamo un grafico degli inquinanti in funzione del tempo

#array per le legende
leg = np.empty(0)
for i in range(len(inq)):
    leg = np.append(leg, tab.columns[i+2])

#array per i colori
col = ('blue', 'orange', 'green', 'red', 'purple', 'black', 'pink')

#disegnamo il grafico dei valori medi degli inquinanti nell'aria rispetto
#al tempo

for i in range(len(inq)):
    plt.plot(t, inq[i], color = col[i], label = leg[i])
plt.xlabel('TEMPO')
plt.ylabel('INQUINANTI (ug/m^3)')
plt.legend()
plt.show()

#calcoliamo la trasformata di fourier per i dati relativi alla CO

tr = sp.fft.fft(inq[0])
dt = t[1] - t[0]
fr = sp.fft.fftfreq(len(inq[0]), d = dt)
#calcoliamo il modulo quadro della trasformata di Fourier per poterne
#disegnare un grafico che ha senso
atr = np.absolute(tr)**2

#disegnamo il grafico della trasformata rispetto alle frequenze
a = sp.fft.fftshift(atr)
b = sp.fft.fftshift(fr)

plt.plot(fr[1:len(atr)//2], atr[1:len(atr)//2])
#plt.plot(b, a, color = 'orange')
#plt.xscale('log')
#plt.yscale('log')
plt.xlabel('FREQUENZA')
plt.ylabel('AMPIEZZA TRASFORMATA (in modulo quadro)')
plt.show()

#disegnamo il grafico in funzione del periodo
#T = 1/freq

per = 1/fr
plt.plot(per, atr)
plt.xlabel('PERIODO')
plt.ylabel('AMPIEZZA TRASFORMATA (in modulo quadro)')
plt.show()

#filtriamo i coafficienti di Fourier, lasciando solo quelli
#che descrivono l'andamento generale in funzione del tempo
#(escludendo fluttuazioni di breve periodo)

#usiamo le maschere

mask = np.absolute(fr) > 0.5*10**(-2)

tr_f = tr.copy()
tr_f[mask] = 0

#calcoliamo la trasforata di fourier inversa a partire dai coefficienti filtrati

inv = sp.fft.ifft(tr_f)
inv_a = np.absolute(inv)

#disegnamo il grafico del segnale ricostruito a partire dai
#coefficienti filtrati sovrapposto al segnale originale

plt.plot(t, inv_a)
plt.plot(t, inq[0])
plt.xlabel('TEMPO')
plt.ylabel('MEAN CO (ug/m^3)')
plt.show()
