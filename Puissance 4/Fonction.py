from graphics.fenetres import *
from graphics.couleurs import *
from random import randint
import numpy as np

#
def tableau_jeux(hauteur,largeur):
    T=np.zeros((hauteur,largeur))    
    return T
#
   
def premier_qui_joue():
    x=randint(0,100)
    if x%2==0 :
        return rouge
    else:
        return jaune
#
def swich_joueur(j) :
    if j == jaune :
        j = rouge
        return j
        
    elif j == rouge:
        j =jaune
        return j
        
def ajouter_boule(T,numero_colonne,joueur):
    l=0
    if joueur == jaune :
        T[l,numero_colonne]=-1
        while l<len(T)-1 and T[l+1,numero_colonne]==0:
            T[l,numero_colonne]=0
            T[l+1,numero_colonne]=-1
            l=l+1
    elif joueur == rouge :
        T[l][numero_colonne]=1
        while l<len(T)-1 and T[l+1,numero_colonne]==0:
            T[l,numero_colonne]=0
            T[l+1,numero_colonne]=1
            l=l+1
    return T
    

def colonnes_pleines(T):
    return not 0 in T[0]
    #renvoi True si le tableau est plein
    
def quatre_en_ligne(T):
    n = len(T)
    p = len(T[0])
    for i in range(n):
        for j in range(p-3):                
            if T[i,j] + T[i,j+1] + T[i,j+2] + T[i,j+3] == 4:
                return rouge
                
            elif T[i,j] + T[i,j+1] + T[i,j+2] + T[i,j+3] == -4:
                return jaune
                

def quatre_en_colonne(T):
    n=len(T)
    p=len(T[0])
    for i in range (p):
        for j in range (n-3):
            if T[j,i]+T[j+1,i]+T[j+2,i]+T[j+3,i]==4 :
                return rouge
                
            elif T[j,i]+T[j+1,i]+T[j+2,i]+T[j+3,i]==-4 :
                return jaune
                
def quatre_en_diag(T):
    n=len(T)
    p=len(T[0])
    for i in range (n-3):
        for j in range (p-3):
            if T[i,j]+T[i+1,j+1]+T[i+2,j+2]+T[i+3,j+3]==4 or T[i+3,j]+T[i+2,j+1]+T[i+1,j+2]+T[i,j+3]==4 :
                return rouge
                
            elif T[i,j]+T[i+1,j+1]+T[i+2,j+2]+T[i+3,j+3]==-4 or T[i+3,j]+T[i+2,j+1]+T[i+1,j+2]+T[i,j+3]==-4 :
                return jaune

def verif_gagnant(T):
    l=quatre_en_ligne(T)
    if l != rouge and l != jaune:
        c=quatre_en_colonne(T)
        if c != rouge and c != jaune:
            d=quatre_en_diag(T)
            if d != rouge and d != jaune:
                return " "
            else :
                return d
        else :
            return c
    else:
        return l
                
def possible_jouer(T,n):
    return 0<=n<=len(T[0])-1 and T[0,n]==0

    
    

