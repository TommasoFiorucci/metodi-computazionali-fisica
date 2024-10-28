# esercizio 1 esercitazione 3


# 1 legga il file kplr010666592-2011240104155_slc.csv e crei il DataFrame pandas corrispondente;

# 2 stampi il nome delle colonne del DataFrame;

# 3 produca un grafico del flusso in funzione del tempo
# suggerimento: usare pyplot.plot;

# 4 produca un grafico del flusso in funzione del tempo coi punti del grafico demarcati da un simbolo (no linea);
# suggerimento: usare pyplot.plot con opzione 'o' o equivalente;

# 5 produca un grafico del flusso in funzione del tempo con barre di errore e salvi il risultato in un file png e/o pdf;
#suggerimento: usare pyplot.errorbar;

# 6 produca un grafico simile al precedente selezionando un intervallo temporale attorno ad uno dei minimi;
# suggerimento: usare .loc per la serezione dei valori nel DataFrame;

# 7 produca un grafico come per il punto 5 ma con la selezione del punto 6 mostrata come riquadro.
# suggerimento: utilizzare inset_axes

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tabella = pd.read_csv('kplr010666592-2011240104155_slc.csv')

#print(tabella)

#print(tabella.columns)

#creo degli array per le coordinate del grafico
forma = tabella.shape
num_elementi = forma[0]

tempo = np.zeros(num_elementi)
for i in range(num_elementi):
    tempo[i] = tabella['TIME'][i]

flusso = np.zeros(num_elementi)
for i in range(num_elementi):
    flusso[i] = tabella['PDCSAP_FLUX'][i]

flusso_err = np.zeros(num_elementi)
for i in range(num_elementi):
    flusso_err[i] = tabella['PDCSAP_FLUX_ERR'][i]

# chiedo a python di disegnare un grafico utilizzando gli array appena definiti

plt.errorbar(tempo, flusso, yerr = flusso_err, fmt = 'o')
plt.xlabel('TEMPO')
plt.ylabel('FLUSSO')

plt.show()

# salvo il grafico come png e pdf

plt.savefig('grafico esopianeta HAT-p-7 b.png')
plt.savefig('grafico esopianeta HAT-p-7 b.pdf')

# chiedo a python di disegnare solo una parte di grafico (uno dei minimi)

tab_rid = tabella.loc[(tabella['TIME'] > 950.25) & (tabella['TIME'] < 950.45)]
#print(tab_rid)

# il metodo usato all'inizio per ricavare le dimensioni della tabella
# non funziona qui

dim_tab = 18582 - 18288
# print(dim_tab)

tempo_rid = np.zeros(dim_tab)
flusso_rid = np.zeros(dim_tab)
flusso_err_rid = np.zeros(dim_tab)
for i in range(18289, 18583):
    tempo_rid[i - 18289] = tabella['TIME'][i]
    flusso_rid[i - 18289] = tabella['PDCSAP_FLUX'][i]
    flusso_err_rid[i - 18289] = tabella['PDCSAP_FLUX_ERR'][i]

plt.errorbar(tempo_rid, flusso_rid, yerr = flusso_err_rid, fmt = 'o')
plt.xlabel('TEMPO')
plt.ylabel('FLUSSO')

plt.show()

# chiedo a python di disegnare il secondo grafico all'interno del primo grafico

fig, ax = plt.subplots(figsize = (12,6))
ins_ax = ax.inset_axes([0.85 , 0.85, 0.3,0.3])
ins_ax.errorbar(tempo_rid, flusso_rid, yerr = flusso_err_rid, fmt = 'o')
ax.errorbar(tempo, flusso, yerr = flusso_err, fmt = 'o')

ins_ax.set_xlabel('TEMPO')
ins_ax.set_ylabel('FLUSSO')
ax.set_xlabel('TEMPO')
ax.set_ylabel('FLUSSO')

plt.show()
