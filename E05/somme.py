# questo file python verrà importato all'interno di Es01.py nella cartella E05

import sys

def somma(n):
    """ è una funzione che calcola la somma dei primi n numeri naturali"""
    s = n * (n + 1) / 2
    return s

def somma_rad(n):
    """ è una funzione che calcola la somma delle radici quadrate dei
    primi n numeri naturali"""
    s = 0
    for i in range(0, n + 1):
        s = s + i**(1/2)
    return s

# modifico questo file, cioè somme.py, per svolgere il secondo esercizio della quinta esercitazione
# aggiungo  delle funzioni

def prodotto(n):
    """ questa funzione calcola il prodotto dei primi n numeri naturali """
    p = 1
    for i in range(1, n + 1):
        p = p * i
    return p

def sommatoria(n, a = 1):
    """ questa funzione calcola la sommatoria da i = 0 ad i = n
    dei numeri naturali i elevati ad a """
    s = 0
    for i in range(0, n + 1):
        s = s + i**a
    return s

sys.path.append("home/lunlun/MCF/metodi-computazionali-fisica/E05")
