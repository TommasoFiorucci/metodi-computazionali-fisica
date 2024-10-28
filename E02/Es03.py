# esercizio 3 esercitazione 2

# calcolo età

# creare uno script python che:
# · chieda in input la vostra data di nascita
# · calcoli la vostra età in anni, giorni, secondi
# · stampi a schermo i risultati con stringhe formattate in modo che
# appaiano incolonnati

# è importante usare la libreria datetime per svolgere questo esercizio

#importiamo la libreria datetime
from datetime import datetime, timedelta

# timedelta permette di calcolare differenze temporali

anno = input("Inserire il proprio anno di nascita: ")
mese = input("inserire il proprio mese di nascita: ")
giorno = input("Inserire il proprio giorno di nascita: ")

data = giorno + "-" + mese + "-" + anno

# ricavo l'anno, il mese, ed il giorno di nascita dalla variabile
# di tipo stringa che ho appena definito

date = datetime.strptime(data, "%d-%m-%Y") #l'anno non può essere troppo vecchio

# se l'orario non è specificato la libreria assume che sia il primo istante di
# quel giorno, cioè il primo secondo di mezzanotte (00:00:00)

data_anno = date.year
data_giorno = date.day
data_secondo = date.second


# calcolo l'età in anni, giorni e poi secondi

data_odierna = datetime.now()

età = data_odierna - date #fornisce il risultato in giorni

età_secondi = età.total_seconds() #abbiamo eliminato l'unità di misura in giorni
età_giorni = età_secondi/(60 * 60 * 24)
età_anni = età_giorni/365

print("la tua età in anni è: ",età_anni, "anni")
print("La tua età in giorni è: ", età_giorni, "giorni")
print("La tua età in secondi è: ", età_secondi, "secondi")

