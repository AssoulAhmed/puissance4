""" réseau côté serveur """
from graphics.fenetres import *
from graphics.couleurs import *
from socket import *


def s(event):
    global connexion_avec_client
    p=Point(event.x,event.y)
    zg.draw_fill_circle(p,50,rouge)
    #création d'un message
    msg_a_envoyer = str(event.x)
    msg_a_envoyer2 = str(event.y)
    msg_a_envoyer = msg_a_envoyer.encode()
    msg_a_envoyer2 = msg_a_envoyer2.encode()
    print(msg_a_envoyer)
    print(msg_a_envoyer2)
    #envoi d'un message
    connexion_avec_client.send(msg_a_envoyer)
    connexion_avec_client.send(msg_a_envoyer2)
    #Attente d'un message
    msg_recu = connexion_avec_client.recv(1024)
    msg_recu2 = connexion_avec_client.recv(1024)
    #décoder et afficher le message
    msg_recu = msg_recu.decode()
    msg_recu2 = msg_recu2.decode()
    print(msg_recu)
    print(msg_recu2)
    j= Point(int(msg_recu),int(msg_recu2))
    zg.draw_fill_circle(j,50,jaune)
    

    
def quit(event):
    connexion_avec_client.close()
    serveur.close()
    f.close()


#Création de la connexion
serveur = socket(AF_INET,SOCK_STREAM)
serveur.bind(('',12800))
serveur.listen(5)
connexion_avec_client, infos_connexion = serveur.accept()

connexion_avec_client.send(b"Je viens d'accepter la partie")
print ("{} connected".format( infos_connexion ))



f=Fenetre()
zg=f.graphique(largeur=500,hauteur=500,couleur=black)
f.title('Serveur')



zg.bind('<Button-1>',s)
zg.bind('<Button-3>',quit)
f.mainloop()





    #faire split 

