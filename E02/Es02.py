# esercizio 2 esercitazione 2

# somma dei primi n numeri naturali

# si calcoli la somma dei primi n numeri naturali

def somma(a):
    s = a*(a + 1)/2
    return s

n = input("Inserire un numero naturale: ")

# n è una variabile di tipo stringa, devo convertirla in una variabile di tipo
#float per poterla usare in delle operazioni matematiche

nf = float(n)

somma_num = somma(nf)

print("la somma dei primi ", n, " numeri naturali è: ", somma_num)
