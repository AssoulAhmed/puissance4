import winsound

def sonpion():
    dic ={'1':'sonp4.wav'}
    for i in ['1']:
        winsound.PlaySound(dic[i],winsound.SND_FILENAME)
    while i in ['<Return>','2','3']:
        i = input("entrer un nombre\n")
        winsound.PlaySound(dic[i],winsound.SND_FILENAME)
    
def felicitation():
    dic ={'1':'Felicitation.wav'}
    for i in ['1']:
        winsound.PlaySound(dic[i],winsound.SND_FILENAME)
    while i in ['<Return>','2','3']:
        i = input("entrer un nombre\n")
        winsound.PlaySound(dic[i],winsound.SND_FILENAME)