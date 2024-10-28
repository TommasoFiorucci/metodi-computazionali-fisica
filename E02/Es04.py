# esercizio 4 esercitazione 2

# liste e dizionari

# sviluppare uno script python che:
# ·crei una lista con i nomi dei giorni della settimana
# ·crei una lista con il nome dei giorni della settimana per tutto il mese
# di ottobre 2024
# ·crei un dizionario che metta in relazione il giorno del mese di ottobre 2024
# con il giorno della settimana

settimana = ["lunedì", "martedì", "mercoledì", "giovedì", "venerdì", "sabato", "domenica"]

n = 0

settimana_ott = ["martedì"]

for i in range(2, 32):
    r = i % 7
    if r == 0:
        n = n + 1
        settimana_ott.append(settimana[i - n * 7])
    else:
        settimana_ott.append(settimana[i - n * 7])

mese = [1]
for i in range(2, 32):
    mese.append(i)


ottobre = { mese[i] : settimana_ott[i] for i in range(len(mese)) }

print(ottobre)
