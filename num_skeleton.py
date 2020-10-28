'''
 Numerov method
'''
import matplotlib.pyplot as plt
import numpy as np
import math

## La proposta di implementazione e' divisa quattro step
## Step 1 (S1)
## Step 2 (S2)
## Step 3 (S3)
## Step 4 (S4)
## il doppio ## indice un commento mentre # indica una
## comando gia' pronto, utilizzabile quando le parti
## precedenti sono completate

def V(xi):
##S1 da riempire     
    return 0

def b(eps,xi):
##S1 da riempire
##   calcolo di b a partire a E (eps), xi e h (globale)    
    return 0

def numerov(n1,n2,eps):
##S1/S2 da completare: riempe i valori di psi(xi) da i=n1 a i=n2 (compresi entrambi)
    psi = np.array(xi)*0  ## copio xi in psi e ne annullo le componenti
    j   = 1               ## intero che definisce incremento: indice i, i+j,i+2*j -> i, i+1, i+2
##S2     definisco indice j in modo che 1 se n2>n1, -1 se n2<n1 (vedi sign di numpy)
##S1/S2  fornisco i primi due valori di psi
##S1/S2  implemento Numerov
#   for i in range(...):
#      psi[i] = 
    return psi

def evalDerivative(eps):
##S3 per energia eps fornita
##   crea sequenza left e right
    global psir,psil
    psil = numerov(0,nmatch+1,eps)
    psir = numerov(n-1,nmatch-1,eps)
##   le normalizza a nmatch
##   ...
##   calcola la differenza (diff) tra le derivate centrate (left e right) in match
##   diff = 0.
##   ...
    return diff

def findE(emin,emax,tol):
##  implementazione di bisezione gia' fornita
    while (emax-emin>tol):
        emed = (emin+emax)/2
        if evalDerivative(emin)*evalDerivative(emed)<0:
            emax = emed
        else:
            emin = emed
    return (emin+emax)/2;
 
## Main code
n       = 14000
nmatch  = 10000
xi      = np.linspace(-7.,7,n)
h       = xi[1]-xi[0]

##S1
#epsilon = 0.5 # o altra energia di stato definito
## Numerov deve funzionare con chiamata
#psi=numerov(0,n-1,epsilon)
## verificare con
#plt.plot(xi,psi)
#plt.show()

##S2
##il passo precedente deve funzionare con sia con 
##  psi = numerov(0,n-1,epsilon)
##che con 
##  psi = numerov(n-1,0,epsilon)


##S3
##commentare i punti precedenti (a parte le definizioni iniziali del Main code
##completare evalDerivative e poi chiamare findE 
#e = findE(1.2,1.7,0.0001)
#print "Energy ", e

##S4
##copiare psr nella parte 'vuota' di psil di modo che psil rappresenti tutta psi(x)
##nell'intervallo dato o, alternativamente, copiarle entrambe in una nuova psi

