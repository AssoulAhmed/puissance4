""" réseau côté serveur """
from graphics.fenetres import *
from graphics.couleurs import *
from socket import *

def deplacement(event):
    p=Point(event.x,event.y)
    zg.draw_fill_circle(p,50,rouge)

def creation_connexion():
    global connexion_avec_client
    #Création de la connexion
    serveur = socket(AF_INET,SOCK_STREAM)
    serveur.bind(('localhost',12800))
    serveur.listen(5)
    connexion_avec_client, infos_connexion = serveur.accept()
    
    connexion_avec_client.send(b"Je viens d'accepter la partie")
    print ("{} connected".format( infos_connexion ))

def envoi_msg_serveur(event):
    global connexion_avec_client
    deplacement(event)
    #création d'un message
    msg_a_envoyer = str(deplacement(event))
    msg_a_envoyer = msg_a_envoyer.encode()
    print(msg_a_envoyer)
    #envoi d'un message
    connexion_avec_client.send(msg_a_envoyer)
    #Attente d'un message
    msg_recu = connexion_avec_client.recv(1024)
    #décoder et afficher le message
    msg_recu = msg_recu.decode()
    print(msg_recu)
    

creation_connexion()

f=Fenetre()
zg=f.graphique(largeur=500,hauteur=500,couleur=black)
f.title('Serveur')

zg.bind('<Button-1>',envoi_msg_serveur)

f.mainloop()