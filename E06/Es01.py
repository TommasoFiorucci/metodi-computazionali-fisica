# esercizio 1 esercitazione 6

# Creare uno script python che:

# 1 legga il file vel_vs_time.csv scaricato;
# 2 produca un grafico della velocità in funzione del tempo;
# 3 calcoli la distanza percorsa in funzione del tempo (utilizzando scipy.integrate.simpson);
# 4 produca il grafico della distanza percorsa in funzione del tempo.
# 5 utilizzare il modulo argparse per permettere di selezionare il garfico da visualizzare o il file da leggere al momento dell'esecuzione.

# SUGGERIMENTO: assicurarsi di comprendere bene il comportamento ella funzione scipy.integrate.simpson agli estremi dell'intervallo di integrazione.

import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

# leggo il file e creo un array per contenere le coordinate temporali e un array per contenere i valori della velocità

tabella = pd.read_csv("vel_vs_time.csv")

l = len(tabella["t"])

velocità = np.zeros(l)
tempo = np.zeros(l)
for i in range(l):
    velocità[i] = tabella["v"][i]
    tempo[i] = tabella["t"][i]

"""facciamo il grafico di v su t"""
plt.plot(tempo, velocità, color = 'green')
plt.xlabel("Tempo")
plt.ylabel("Velocità")
plt.show()
    
# chiedo a python di calcolare la distanza in funzione del tempo
# cioè di calcolare l'integrale di v in dt, usando la regola di cavalieri-simpson

integrale = sp.integrate.simpson(velocità, tempo)

print("Il valore dell'integrale della velocità rispetto al tempo è: ",integrale)

"""calcoliamo lo spazio percorso in funzione del tempo"""

spazio = np.empty(1)
for i in range(1, l):
    speed = velocità[0:i]
    time = tempo[0:i]
    space = sp.integrate.simpson(speed, time)
    spazio = np.append(spazio, space)

"""disegnamo un grafico dello spazio percorso in funzione del tempo"""

plt.plot(tempo, spazio, color = 'green')
plt.xlabel("Tempo")
plt.ylabel("Spazio Percorso")
plt.show()


def parse_arguments():
    parser = argparse.ArgumentParser(description = "utilizzo argparse")
    parser.add_argument("-v", "--vel_tempo", action = "store_true", help = "prova grafico velocità in funzione del tempo")
    parser.add_argument("-x", "--pos_tempo", action = "store_true", help = "mostra il grafico della posizione in funzione del tempo")
    return parser.parse_args()

def main():

    args = parse_arguments()

    if args.vel_tempo == True:

        # chiedo a python di disegnare un grafico della velocità in funzione del tempo
        
        plt.plot(tempo, velocità)
        plt.xlabel("TEMPO")
        plt.ylabel("VELOCITÀ")
    
        plt.show()

    if args.pos_tempo == True:

        # chiedo a python di disegnare un grafico della posizione in funzione del tempo
        
        plt.plot(tempo, spazio)
        plt.xlabel("TEMPO")
        plt.ylabel("SPAZIO")

        plt.show()

        
main()

