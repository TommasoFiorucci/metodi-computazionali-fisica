import sys
import os
import pandas as pd
import numpy as np

class Hit():

    """classe che identifica un modulo, un suo sensore ed il timestamp
    nel quale viene colpito

    parametri:

    modulo = modulo che viene colpito

    sensore = sensore del modulo che viene colpito

    timestamp = istante in cui il sensore del modulo viene colpito"""
    
    def __init__(self):
        self.modulo = 0
        self.sensore = 0
        self.timestamp = 0

    #crea un oggetto Hit standard, con modulo = 0, sensore = 0, timestamp = 0
        
    def __repr__(self):
        return "Rivelatore: {:} + {:} + {:}".format(self.modulo, self.sensore, self.timestamp)
    

    """scrivendo self si ottengono i valori del modulo, sensore e timestamp"""

    def __str__(self):
        return "Rivelatore: {:} - {:} - {:}".format(self.modulo, self.sensore, self.timestamp)

    """scrivendo print(self) si ottengono i valori di modulo, sensore, timestamp
    come una stringa"""

    def riv(self, modulo, sensore, timestamp):
        self.modulo = modulo
        self.sensore = sensore
        self.timestamp = timestamp

    #modifica i valori di modulo, sensore e timestamp di un oggetto Hit

    def __eq__(self, other):
        return self.timestamp == other.timestamp and self.modulo == other.modulo and self.sensore == other.sensore

    """verifica se due oggetti hit sono identici"""

    def __gt__(self, other):
        return self.timestamp > other.timestamp

    #verifica se self è stato colpito dopo other (ad un timestamp maggiore cioè)
    
    def __lt__(self, other):
        return self.timestamp < other.timestamp
    
    #controlla se self è stato colpito prima di other

    def __add__(self, other):
        return self.timestamp + other.timestamp

    #somma i timestamp di self e other

    def __sub__(self, other):
        return self.timestamp - other.timestamp

    #sottrae il timestamp di other al timestamp di self

sys.path.append('/home/lunlun/MCF/metodi-computazionali-fisica/E05')
    
