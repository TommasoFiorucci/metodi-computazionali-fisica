# esercizio 1 esercitazione 8

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import V_input
import pandas as pd

# risolvo l'equazione differenziale per V_out dato V_in

# chiedo a python di risolvere l'equazione differenziale
# usando il metodo scipy.integrate.odeint

a = 0
b = 10
n = 100

h = (b - a) / n
tempo = np.arange(a, b, h)

V_out_0 = 0

''' per definire la funzione vin usiamo un modulo, che verrà poi importato
all'interno di questo codice'''

#definiamo la funzione che sta a secondo membro dell'equazione differenziale

def fode(vout, *t):
    '''é la funzione che sta a secondo membro dell'equazione differenziale

    vout = voltaggio in output
    t = array temporale, argomento di vin
    r = resistenza del circuito
    c = capacità del circuito (del condensatore) '''

    V_out = np.empty(0)
    for i in range(len(t)):
        Vout = V_input.vin(t[i]) + vout
        V_out = np.append(V_out, Vout)

    return V_out

#calcoliamo la soluzione dell'equazione differenziale
#e disegnamo il grafico di vout e vin in funzione del tempo
rc = np.array([1, 0.5, 0.1]) #vari valori di rc
sol = sp.integrate.odeint(fode, y0 = V_out_0, t = tempo) #soluzione

#calcoliamo la soluzione per ogni valore di rc
s = {} #visto che sol è un array anche
        #i sigoli elementi di s devono
        #essere degli array, quindi rendiamo s un dizionario
for i in range(len(rc)):
    s_i = (1/rc[i])*sol #soluzione vera
    #aggiungiamo l'elemento s_i al dizionario
    s.update({i : s_i})

#disegnamo il grafico di vout per ogni soluzione
#cioè per ogni valore di rc

fig, ax = plt.subplots(1, 3, figsize=(24, 6))

ax[0].plot(tempo, s[0])
ax[0].set_title('RC = 1')
ax[0].set_xlabel('TEMPO')
ax[0].set_ylabel('V_out')

ax[1].plot(tempo, s[1])
ax[1].set_title('RC = 0,5')
ax[1].set_xlabel('TEMPO')
ax[1].set_ylabel('V_out')

ax[2].plot(tempo, s[2])
ax[2].set_title('RC = 0,1')
ax[2].set_xlabel('TEMPO')
ax[2].set_ylabel('V_out')

plt.show()

#disegnamo i tre grafici sovrapposti l'uno all'altro

for i in range(len(rc)):
    plt.plot(tempo, s[i])

plt.xlabel('TEMPO')
plt.ylabel('V_out')
plt.show()

#disegnamo il grafico di vin in funzione del tempo
v = np.empty(0)
for i in range(len(tempo)):
    vi = V_input.vin(tempo[i])
    v = np.append(v, vi)
plt.plot(tempo,v)
plt.xlabel('TEMPO')
plt.ylabel('V_in')
plt.show()

print(tempo)

#salviamo i valori di t, V_out e V_in in in file csv (per tutti i valori di rc)
#creiamo una tabella contenente questi valori

tabella = pd.DataFrame(columns = ['Tempo', 'V input', 'V out (RC=1)', 'V out (RC=0,5)', 'V out (RC=0,1)'])

tabella['Tempo'] = tempo
tabella['V input'] = v
tabella['V out (RC=1)'] = s[0]
tabella['V out (RC=0,5)'] = s[1]
tabella['V out (RC=0,1)'] = s[2]

print(tabella)

#rendiamo la tabella un file .csv

tabella.to_csv('tabella voltaggi Es01.csv')


