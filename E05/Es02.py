# esercizio 2 esercitazione 5

# Modificare il file somme.py aggiungendo:
# una funzione che restituisca la somma e il prodotto dei primi n numeri
# naturali, con n da passare tramite un argomento;

# una funzione che restituisca 
# sum(i = 0, n, i**a) con n da passare tramite un argomento e a 
# da passare come argomento opzionale con valore di default pari a 1.

# Modificare lo script python che importa il modulo somme in modo
# da utilizzare le funzioni appena create.

# io invece creo un nuovo file uwu

import somme

n_str = input("Inserire un numero naturale n: ")
a_str = input("(opzionale) Inserire un numero reale a: ")

n = int(n_str)
a = float(a_str)

somma = somme.somma(n)
prodotto = somme.prodotto(n)
sommatoria = somme.sommatoria(n, a)

print("La somma dei primi ", n, " numeri naturali è: ", somma)
print("Il prodotto dei primi ", n, " numeri naturali è: ", prodotto)
print("La sommatoria dei primi ", n, " numeri naturali elevati a ", a, " è: ", sommatoria)


