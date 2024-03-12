""" réseau côté client """
from graphics.fenetres import *
from graphics.couleurs import *
from socket import *

# la bibliothèque socket permet de programmer des applications réseau
def deplacement(event):
    p=Point(event.x,event.y)
    zg.draw_fill_circle(p,50,rouge)

def connexion_client():
    global client
    #Création de la connexion
    client = socket(AF_INET,SOCK_STREAM)
    
    # Connexion au serveur
    # écrire l'dresse IP du serveur : 4 octets:
    # par exemple 168.192.10.1
    # Pour savoir l'adresse IP d'une carte réseau : dans la fenêtre de commande windows
    # taper ipconfig /all
    host = 'localhost'
    client.connect((host,12800))

def envoi_msg_client(event):
    global client
    deplacement(event)
    #création d'un message
    msg_a_envoyer = str(deplacement(event))
    msg_a_envoyer = msg_a_envoyer.encode()
    #écriture du message reçu
    print(msg_a_envoyer)
    #envoyer un messagee
    client.send(msg_a_envoyer)
    # Attente d'un message
    msg_recu = client.recv(1024)
    #Decoder et afficher le message recu
    msg_recu = msg_recu.decode()
    print(msg_recu)
    

    
connexion_client()

f=Fenetre()
zg=f.graphique(largeur=500,hauteur=500,couleur=black)
f.title('Client')

zg.bind('<Button-1>',envoi_msg_client)

f.mainloop()