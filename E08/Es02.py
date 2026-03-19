import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

#scriviamo l'array temporale che useremo per risolvere l'equazione differenziale

a = -20
b = 20
n = 400
h = (b-a)/n

tempo = np.arange(a, b, h)

#definiamo la funzione a secondo membro dell'equazione differenziale

def fode(r, t):
    ''' l'equazione differenziale è del secondo ordine
    può essere scritta come un sistema di equazioni differenziali del primo
    ordine. le eq diff di questo sistema possono essere scritte come le
    componenti di un'eq diff vettoriale

    theta = angolo del pendolo = r[0]
    omega = velocità angolare del pendolo = r[1]

    dthetadt = dtheta/dt
    domegadt = domega/dt
    '''
    dthetadt = r[1]
    domegadt = (-sp.constants.g)*np.sin(r[0])

    return (dthetadt, domegadt)

#definiamo le condizioni iniziali del sistema (dell'eq diff)

yinit = (np.radians(45), 0) #np.radians per convertire l'angolo
                            #da gradi in radianti
l = 0.5
#risolviamo l'equazione differenziale

sol = sp.integrate.odeint(fode, y0 = yinit, t = tempo)
s = sol/l

#disegnamo il grafico di theta in funzione di t

plt.plot(tempo, s[:,0])
plt.xlabel('TEMPO')
plt.ylabel('ANGOLO THETA')
plt.show()

#risolviamo l'eq diff per 3 diverse condizioni iniziali

r0 = {0 : [np.radians(45), 0], 1 :  [np.radians(45), 0], 2 : [np.radians(30),0]}
L = np.array([0.5, 1, 0.5])
S = {} #dizionario contenente le soluzioni per ogni set di condizioni iniziali
for i in range(len(L)):
    soluz = sp.integrate.odeint(fode, y0 = r0[i], t = tempo)
    s_i = soluz/L[i]
    #aggiungiamo le soluzioni al dizionario
    S.update({i : s_i})

#disegnamo i grafici delle 3 soluzioni

ang = np.array([45, 45, 30]) #array con gli angoli iniziali in gradi
                   #per poter scrivere la legenda del grafico in
                   #maniera più facile da leggere

for i in range(len(L)):
    plt.plot(tempo, S[i][:, 0], label = ('l =', L[i], ' θ =', ang[i], ' ω =', r0[i][1]))
plt.xlabel('TEMPO')
plt.ylabel('ANGOLO θ')
plt.legend(loc = 'upper center')
plt.show()
