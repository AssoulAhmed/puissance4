from graphics.fenetres import *
from graphics.couleurs import *
from random import randint
from Fonction import *
from son import *

def setup(T,lg,ht,f):
    #Fond
    global zg
    
    zg=f.graphique(largeur=100*(lg+1.5),hauteur=100*(ht+2.5),couleur=noir)
    
    #plateau
    pl1,pl2=Point(0,100),Point(100*(lg+2),100*(ht+3))
    zg.draw_fill_rectangle(pl1,pl2,bleu)
    affiche(T,ht,lg)


def affiche(T,hauteur,largeur):
    for i in range(hauteur):
        for j in range(largeur):
            if T[i][j]==0:
                pion=Point(j*120+60,i*120+160)
                zg.draw_fill_circle(pion,50,blanc)           
            elif T[i][j]==-1:
                pion=Point(j*120+60,i*120+160)
                zg.draw_fill_circle(pion,50,jaune)
            elif T[i][j]==1:
                pion=Point(j*120+60,i*120+160)
                zg.draw_fill_circle(pion,50,rouge)

def deplacement(event):
    global pion
    global lg
    global ht
    global colonne
    global T
    global joueur
    global c
    global G
    global E
    reste = 0
    zg.efface(c)
    
    if G!=rouge and G!=jaune and E!=True:
    
        if pion.x > 100 and event.keysym == 'Left':
            pion.x -= 120
            colonne=colonne-1
            c=zg.draw_fill_circle(pion,50,joueur)            
       
        elif pion.x < (100+(120*(lg-1.5))) and event.keysym == 'Right' :
            pion.x += 120
            colonne=colonne+1
            c=zg.draw_fill_circle(pion,50,joueur)            
            
        elif event.keysym == 'Return':
            
            if possible_jouer(T,colonne):
    
                T=ajouter_boule(T,colonne,joueur)
                affiche(T,ht,lg)
                joueur=swich_joueur(joueur)
                G=verif_gagnant(T)
                E=colonnes_pleines(T)
                c=zg.draw_fill_circle(pion,50,joueur) 
                
                if G==rouge or G==jaune or E==True :
                      affiche_g()   
            else :
                c=zg.draw_fill_circle(pion,50,joueur)
                
            sonpion()    
    else:
        affiche_g ()
        felicitation()
        if event.keysym == 'Return':
            f.destroy()
        
        
                    
    
def base(long,haut,tab,win):
    global c
    global joueur
    global pion
    global colonne
    global lg
    global ht
    global G
    global E
    global T
    global f
    f=win
    T=tab
    ht=haut
    lg=long
    joueur=premier_qui_joue()
    pion=Point(180,50)
    c=zg.draw_fill_circle(pion,50,joueur)
    colonne=1
    G=""
    E=""    
    zg.activer_clavier()
    zg.bind('<Key>',deplacement)

def affiche_g ():
    #fonction qui affichent le gagnant
    global zg
    global joueur
    zg=f.graphique(largeur=700,hauteur=600,couleur=noir)
    P1=Point(350,300)
    if G==rouge:
        zg.aff_texte("Rouge tu as gagné",P1,taille=50,couleur=rouge,gras=Y)
        joueur=swich_joueur(joueur)
    elif G==jaune:
        zg.aff_texte("Jaune tu as gagné",P1,taille=50,couleur=jaune,gras=Y)
        joueur=swich_joueur(joueur)
    
    elif E==True:
        zg.aff_texte("Egalité !!!",P1,taille=50,couleur=blanc,gras=Y)