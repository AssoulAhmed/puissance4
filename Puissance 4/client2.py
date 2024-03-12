""" réseau côté client """
from graphics.fenetres import *
from graphics.couleurs import *
from socket import *

# la bibliothèque socket permet de programmer des applications réseau
def pion(event):
    global client
    p=Point(event.x,event.y)
    zg.draw_fill_circle(p,50,jaune)
    #création d'un message
    msg_a_envoyer = str(event.x)
    msg_a_envoyer2 = str(event.y)
    msg_a_envoyer = msg_a_envoyer.encode()
    msg_a_envoyer2 = msg_a_envoyer2.encode()
    print(msg_a_envoyer)
    print(msg_a_envoyer2)
    #envoi d'un messagee
    client.send(msg_a_envoyer)
    client.send(msg_a_envoyer2)
    #Attente d'un message
    msg_recu = client.recv(1024)
    msg_recu2 = client.recv(1024)
    msg_recu = msg_recu.decode()
    msg_recu2 = msg_recu2.decode()
    print(msg_recu)
    print(msg_recu2)
    r= Point(int(msg_recu),int(msg_recu2))
    zg.draw_fill_circle(r,50,rouge)
    
    

#Création de la connexion
client = socket(AF_INET,SOCK_STREAM)

# Connexion au serveur
# écrire l'dresse IP du serveur : 4 octets:
# par exemple 168.192.10.1
# Pour savoir l'adresse IP d'une carte réseau : dans la fenêtre de commande windows
# taper ipconfig /all

client.connect(('localhost',12800))


f=Fenetre()
zg=f.graphique(largeur=500,hauteur=500,couleur=black)
f.title('Client')


zg.bind('<Button-1>',pion)
f.mainloop()





#client.close()