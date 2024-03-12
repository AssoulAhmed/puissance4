from graphics.fenetres import *
from graphics.couleurs import *
from random import randint
from Fonction import *
from p4 import *



def Jeux_Local():
    f=Fenetre()
    f.title("Puissance 4")
    lg=7
    ht=6
    T=tableau_jeux(ht,lg)
    setup(T,lg,ht,f)
    base(lg,ht,T,f)
    f.mainloop()

    
