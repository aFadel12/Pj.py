
import random


lettres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
chiffres = "0123456789"
symboles = "!@#$%^&*()_+-=[]{};:,./?"


longueur = int(input("Entrez la longueur du mot de passe (entre 8 et 32) : "))
chiffres_oui = input("Voulez-vous inclure des chiffres ? (oui/non) : ")
symboles_oui = input("Voulez-vous inclure des symboles ? (oui/non) : ")


if longueur < 8 or longueur > 32:
    print("Longueur invalide. Le mot de passe doit avoir entre 8 et 32 caractères.")
    exit()


mot_de_passe = []


for i in range(longueur):
    mot_de_passe.append(random.choice(lettres))


if chiffres_oui.lower() == "oui":

    nb_chiffres = random.randint(1, longueur // 2)
   
    indices = random.sample(range(longueur), nb_chiffres)
 
    for indice in indices:
        mot_de_passe[indice] = random.choice(chiffres)


if symboles_oui.lower() == "oui":

    nb_symboles = random.randint(1, longueur // 4)
    
    indices = random.sample(range(longueur), nb_symboles)
  
    for indice in indices:
        mot_de_passe[indice] = random.choice(symboles)

mot_de_passe = "".join(mot_de_passe)

print("Votre mot de passe est : " + mot_de_passe)
