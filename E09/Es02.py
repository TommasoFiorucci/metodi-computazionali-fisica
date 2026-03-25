import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt

#scriviamo le tablle delle 6 sorgenti

#le tabelle da 1 a 3 sono per la classe BLL
#le tabelle da 4 a 6 sono per la classe FRSQ

#sorgente PKS 0426-380, classe BLL
tab1 = pd.read_csv('4FGL_J0428.6-3756_weekly_9_15_2023_mcf.csv')
#sorgente S5 0716+71, classe BLL
tab2 = pd.read_csv('4FGL_J0721.9+7120_weekly_9_15_2023_mcf.csv')
#sorgente Bl Lac, classe BLL
tab3 = pd.read_csv('4FGL_J2202.7+4216_weekly_9_15_2023_mcf.csv')
#sorgente 3C 279, classe FRSQ
tab4 = pd.read_csv('4FGL_J1256.1-0547_weekly_9_15_2023_mcf.csv')
#sorgente CTA 102, classe FRSQ
tab5 = pd.read_csv('4FGL_J2232.6+1143_weekly_9_15_2023_mcf.csv')
#sorgente 3C 454.3, classe FRSQ
tab6 = pd.read_csv('4FGL_J2253.9+1609_weekly_9_15_2023_mcf.csv')

print(tab1)

#creiamo dei dizionari per immagazzinare le informazioni delle tabelle
#e per poterle usare in maniera più efficiente e rapida più tardi
#(usando dei cicli for per esempio)

diz = {0 : tab1, 1 : tab2, 2 : tab3, 3 : tab4, 4 : tab5, 5 : tab6}

tempo = {}
flusso = {}

for i in range(len(diz)):
    tempo.update({i : diz[i]['Julian Date']})
    flusso.update({i : diz[i]['Photon Flux [0.1-100 GeV](photons cm-2 s-1)']})

#generiamo un grafico di tutte le curve sovrapposte

#creiamo un array con le stringhe da usare come legenda
leg = ('sorgente PKS 0426-380, classe BLL', 'sorgente S5 0716+71, classe BLL', 'sorgente Bl Lac, classe BLL', 'sorgente 3C 279, classe FRSQ', 'sorgente CTA 102, classe FRSQ', 'sorgente 3C 454.3, classe FRSQ')

#facciamo lo stesso con i colori delle curve
col = ('blue', 'orange', 'green', 'black', 'pink', 'red')

for i in range(len(diz)):
    plt.plot(tempo[i], flusso[i], color = col[i], label = leg[i])
plt.xlabel('GIORNO GIULIANO')
plt.ylabel('FLUSSO (photons cm-2 s-1)')
plt.legend()
plt.show()

#disegnamo un grafico di tutte le curve sovrapposte, ma coloriamo
#le sorgenti appartenenti alle classi BLL e le FRSQ con colori diversi

for i in range(len(diz)):
    if i <= 2:
        plt.plot(tempo[i], flusso[i], color = col[0], label = leg[i])
    else:
        plt.plot(tempo[i], flusso[i], color = col[1], label = leg[i])
plt.xlabel('GIORNO GIULIANO')
plt.ylabel('FLUSSO (photons cm-2 s-1)')
plt.legend()
plt.show()

#calcoliamo le trasformate di fourier delle curve di luce

#dizionario contenente le trasformate dei segnali
tf = {}  
#dizionario contenente gli array delle frequenze di campionatura usate per
#calcolare le trasformate di Fourier delle curve
fr = {}
for i in range(len(diz)):
    #rendiamo l'array flusso[i] un array numpy prima di metterlo
    #come argomento di sp.fft.fft()
    fl = np.array(flusso[i])
    tras = sp.fft.fft(fl)
    #intervallo temporale tra le frequenze di campionatura che prendiamo
    #in considerazione
    dt = tempo[i][1] - tempo[i][0]
    freq = sp.fft.fftfreq(len(fl), d = dt)
    tf.update({i : tras})
    fr.update({i : freq})

#calcoliamo il modulo quadrato delle trasformate, così da poterne disegnare
#un grafico che abbia senso, visto che i coefficienti in generale
#sono numeri complessi

tfr = {} 
frr = {}
for i in range(len(diz)):
    trasr = np.absolute(tf[i])**2
    freqr = np.absolute(fr[i])**2
    tfr.update({i : trasr})
    frr.update({i : freqr})

#disegnamo il grafico delle trasformate di fourier (in modulo quadro) dei
#vari segnali sovrapposte

for i in range(len(diz)):
    if i <= 2:
        plt.plot(frr[i], tfr[i], color = col[0], label = leg[i])
    else:
        plt.plot(frr[i], tfr[i], color = col[1], label = leg[i])
plt.xlabel('FREQUENZE')
plt.ylabel('AMPIEZZA TRASFORMATA (in modulo quadro)')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()

#normalizziamo le trasformate di fourier dei segnali ai loro coefficienti
#di ordine zero

tfrn = {}
for i in range(len(diz)):
    tn = tfr[i]/tfr[i][0]
    tfrn.update({i : tn})

#disegnamo il grafico di questi spettri di potenza sovrapposti
#sempre differenziando le sorgenti appartenenti alle classi BLL e FSRQ
#tramite i colori

for i in range(len(diz)):
    if i <= 2:
        plt.plot(frr[i], tfrn[i], color = col[0], label = leg[i])
    else:
        plt.plot(frr[i], tfrn[i], color = col[1], label = leg[i])
plt.xlabel('FREQUENZE')
plt.ylabel('AMPIEZZA TRASFORMATA (in modulo quadro)')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.show()
