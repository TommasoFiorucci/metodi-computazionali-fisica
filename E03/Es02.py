# esercizio 2 esercitazione 3

# 1 legga il file ExoplanetsPars_2024.csv e crei il DtaFrame pandas corrispondente;
#suggerimento: usare l'opzione comment='#'

# 2 stampi il nome delle colonne del DataFrame;

# 3 stampi un estratto del contenuto del DataFrame;

# 4 produca un grafico con assi logaritmici della massa del pianeta in funzione del periodo orbitale;
#suggerimento: usare pyplot.scatter;

# 5 produca un grafico con assi logaritmici della grandezza (R_max^2)/m in funzione del periodo orbitale;
# R_max : Orbit Semi-Major Axis
# m_i : Stellar Mass

# 6 produca un grafico con assi logaritmici della massa del pianeta in funzione del periodo orbitale distinguendo gli esopianeti per metodo di scoperta (Transit o Radial Velocity) con la corrispondente legenda (gli altri tipi di esopianeti non vanno considerate nel grafico);
#suggerimento: usare .loc per la serezione dei valori nel DataFrame;
#suggerimento: usare l'opzione alpha per la trasparenza;

# 7 produca l'istogramma sovrapposto della massa del pianeta distinguendo gli esopianeti per metodo di scoperta (Transit o Radial Velocity) con la corrispondente legenda con la relativa legenda;
#suggerimento: usare pyplot.hist definendo lo stesso numero di bin e lo stesso intervallo per l'asse x;
#suggerimento: usare l'opzione alpha per la trasparenza;

# 8 produca un grafico analogo al precedente per il logaritmo in base 10 della massa del pianeta.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
