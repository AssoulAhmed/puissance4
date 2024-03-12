from graphics.fenetres import *
from graphics.couleurs import *
from random import randint
from Jeux import *


f= Fenetre()

##Arrière plan

#Trou 

def trou(x,y):
    trou=Point(x,y)
    contour=Point(x-3,y-3)
    ombre=Point(x-10,y-10)
    zg.draw_fill_circle(contour,50,noir)
    zg.draw_fill_circle(trou,50,blanc)

#Plateau et trous

def plateau(taille):
    h=100
    for j in range(taille):    
        v=200
        for i in range(taille):
            trou(h,v)
            v=v+120
        h=h+120    
sol1,sol2,sol3=Point(0,500),Point(700,800),Point(700,500)
zg=f.graphique(largeur=700,hauteur=600,couleur=bleu)
plateau(5)

text=Point(350,50)
zg.aff_texte('PUISSANCE 4',text,taille=50,couleur=rouge,gras=Y)
zg.draw_fill_rectangle(sol1,sol2,bleu)
zg.draw_line(sol1,sol3,noir)

##Bouton 'Lan'

def lan():
    global b1
    global b2
    
    #Suppression des boutons 'Lan' et 'Local'
    
    b1.destroy()
    b2.destroy()
    
    #Bouton 'Créer serveur'
    
    b3 = f.bouton(commande=creer ,texte="Créer serveur",largeur = 20,hauteur=5,alignement ='droite_bas')
    b3.configure(bg = rouge) 
    b3.configure(fg = noir) 
    
    #Bouton 'Rejoindre serveur'
    
    b4 = f.bouton(commande=rejoin ,texte="Rejoindre serveur",largeur = 20,hauteur=5,
    alignement ='gauche_bas')
    b4.configure(bg = jaune) 
    b4.configure(fg = noir) 

##Bouton du menu

#Bouton 'Quitter'

b = f.bouton(commande=f.destroy ,texte="Quitter",largeur = 20,hauteur=5,
alignement ='bas')
b.configure(bg = bleu) 
b.configure(fg = rouge) 

#Bouton 'Local'

b1 = f.bouton(commande=Jeux_Local ,texte="Local",largeur = 20,hauteur=5,
alignement ='droite_bas')
b1.configure(bg = bleu) 
b1.configure(fg = rouge) 

#Bouton 'Lan'

b2 = f.bouton(commande=lan ,texte="Lan",largeur = 20,hauteur=5,
alignement ='gauche_bas')
b2.configure(bg = bleu) 
b2.configure(fg = rouge) 



##Animation des pions

#Liste de couleur

numCouleur=0
couleur=[rouge,jaune]

#Déplacement des pions

def deplacement():

    global pion
    global c
    global numCouleur
    zg.efface(c)
    pion.x += 10
    c = zg.draw_fill_circle(pion,50,couleur[numCouleur])
    while pion.x >= 750 :
        pion.x = -50    
        
        #Changement de couleurs
        
        numCouleur = numCouleur +1    
        numCouleur = numCouleur % len(couleur)
    
    zg.after(50,deplacement)

pion=Point(350,450)
c = zg.draw_fill_circle(pion,50,couleur[numCouleur])
zg.after(50,deplacement)

##Jeu

f.mainloop() 
 
 
 
 
    






