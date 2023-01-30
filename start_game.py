# afficher le contexte et le début de l'histoire
# ask_name()
# move()

from random import randint
def start_game():
   global personnage
   print("les personnages sont: mario, luidgi, daisy, pitch!")
   personnage = input("Veuillez saisir le nom du personnage de votre choix:")
   if personnage == "mario":
      print("vous avez choisit mario!")
      print("Votre personnage s'affichera sur l'ecran avec un (M)!")
      personnage = "M"
   elif personnage == "luidgi":
      print("vous avez choisit luidgi!")
      print("Votre personnage s'affichera sur l'ecran avec un (L)!")
      personnage = "L"
   elif personnage == "daisy":
      print("vous avez choisit daisy!")
      print("Votre personnage s'affichera sur l'ecran avec un (D)!")
      personnage = "D"
   elif personnage == "pitch":
      print("vous avez choisit pitch")
      print("Votre personnage s'affichera sur l'ecran avec un (P)!")
      personnage = "P"
   else:
      input("Erreur! Veuillez saisir le nom d'un personnage entre mario, luigi, daisy et pitch:")

def initialise_game(lignes, colonnes, tableau):
   for i in range(lignes):
      lst = []
      for j in range(colonnes):
         lst.append("X")
      tableau.append(lst)

'''def insere_personnage(ligne, colonne, tatazizi):
   tatazizi[ligne][colonne] = personnage
   #affecter une valeur dans un tableau checker si c bien comme ca
'''
def affiche_tableau(lignes, colonnes, tableau):
   for i in range(lignes):
      for j in range(colonnes):
         print(tableau[i][j], end = "")
      print()

def position_depart_personnage(l, h, tableau):
   tableau[l][h] = personnage

def move_player(direction, coordon_ligne, coordon_colonne, limit_down, limit_right, tableau):
   key_value = key_move_player(direction)
   if key_value == 8 and coordon_ligne > 0:
      tableau[coordon_ligne - 1][coordon_colonne] = personnage
      tableau[coordon_ligne][coordon_colonne] = "X"
      coordon_ligne -= 1
      #print("modif coord ligne : ", coordon_ligne)
      return coordon_ligne
   if key_value == 2  and coordon_ligne < limit_down:
      tableau[coordon_ligne + 1][coordon_colonne] = personnage
      tableau[coordon_ligne][coordon_colonne] = "X"
      coordon_ligne += 1
      #print("modif coord ligne : ", coordon_ligne)
      return coordon_ligne
   if key_value == 6  and coordon_colonne < limit_right:
      tableau[coordon_ligne][coordon_colonne+1] = personnage
      tableau[coordon_ligne][coordon_colonne] = "X"
      coordon_colonne += 1
      #print("modif coord colonne : ", coordon_colonne)
      return coordon_colonne
   if key_value == 4  and coordon_colonne > 0:
      tableau[coordon_ligne][coordon_colonne-1] = personnage
      tableau[coordon_ligne][coordon_colonne] = "X"
      coordon_colonne -= 1
      #print("modif coord colonne : ", coordon_colonne)
      return coordon_colonne

def key_move_player(direction):
   if direction == "8":
      return 8
   if direction == "2":
      return 2
   if direction == "6":
      return 6
   if direction == "4":
      return 4

def ennigme_A(ligne, colonne, tableau):
   print("                                      ", "Vous êtes tombés sur l'ennemi: Aladin!")
   print("                                           le défis d'Aladin est le suivant: ")
   print("                                            Trouve la bonne réponse de l'énigme:")
   print("                                           Si tu a faux tu revient à la case de départ!")
   B = randint(1, 5)
   if B == 1:
      print("                                   Toute chose, il dévore. Il ronge le fer, fait disparaître l’acier,")
      print("                                       et réduit les pierres en poussière. Qui est-ce?")
      print("                                         1 - Un dragon")
      print("                                         2 - Une pomme")
      print("                                         3 - Le temps")
      w = int(input("                                      Veuillez choisir le numéro de la réponse:"))
      if w == 3:
         print("Bonne réponse!")
         return True
      else:
         print("Faux! Vous revenez à la case de départ!")
         tableau[ligne][colonne] = personnage
         return False

   elif B == 2:
      print("                                   Qu'est-ce qui commence la nuit et termine le matin?")
      print("                                     1- les étoiles")
      print("                                     2- N")
      print("                                     3- la nuit")
      w = int(input("                                      Veuillez choisir le numéro de la réponse:"))
      if w == 2:
         print("Bonne réponse!")
         return True
      else:
         print("Faux! Vous revenez à la case de départ!")
         tableau[ligne][colonne] = personnage
         return False

   elif B == 3:
      print("                                   Quel son les couleur primaire?")
      print("                                   1- orange,jaune et bleue")
      print("                                   2- noir et blanc")
      print("                                   3- rouge,jaune et bleue")
      w = int(input("                                      Veuillez choisir le numéro de la réponse:"))
      if w == 3:
         print("Bonne réponse!")
         return True
      else:
         print("Faux! Vous revenez à la case de départ!")
         tableau[ligne][colonne] = personnage
         return False

   elif B == 4:
      print("                                   On peut l'entendre, l'utiliser pour faire du bruit avec, mais ne pas la voir:")
      print("                                   1- La voix")
      print("                                   2- le vent")
      print("                                   3- un piano")
      w = int(input("                                      Veuillez choisir le numéro de la réponse:"))
      if w == 1:
         print("Bonne réponse!")
         return True
      else:
         print("Faux! Vous revenez à la case de départ!")
         tableau[ligne][colonne] = personnage
         return False

   else:
      print("                                   Quel couleur symbolise la mort en Asie?")
      print("                                   1- Le noir")
      print("                                   2- Le gris")
      print("                                   3- Le blanc")
      w = int(input("                                      Veuillez choisir le numéro de la réponse:"))
      if w == 3:
         print("Bonne réponse!")
         return True
      else:
         print("Faux! Vous revenez à la case de départ!")
         tableau[ligne][colonne] = personnage
         return False

def ennigme_B():
   print("                                      ", "Vous êtes tomber sur l'ennemi: Bowzer!")
   B = randint(1, 4)
   if B == 1:
      print("                                           le défis de Bowzer est le suivant: ")
      print("                                          Trouvez le mot qui à une faute d'orthographe:")
      print("                                            Si tu a faux tu recule de 8 cases!")
      print("                                      1- Arrogant")
      print("                                      2- Charlatan")
      print("                                      3- Gentil")
      print("                                      4- Bryant")
      w = int(input("                                      Veuillez choisir le numéro de la réponse:"))
      if w == 4:
         print("Bonne réponse!")
      else:
         print("Faux! Vous reculez de 8 cases!")

   elif B == 2:
      print("                                           le défis de Bowzer est le suivant: ")
      print("                                          Trouvez le mot qui à une faute d'orthographe:")
      print("                                            Si tu a faux tu recule de 8 cases!")
      print("                                      1- Passionnant")
      print("                                      2- Atirant")
      print("                                      3- Délirant")
      w = int(input("                                      Veuillez choisir le numéro de la réponse:"))
      if w == 2:
         print("Bonne réponse!")
      else:
         print("Faux! Vous reculez de 8 cases!")

   elif B == 3:
      print("                                           le défis de Bowzer est le suivant: ")
      print("                                               Trouvez le mot qui existe:")
      print("                                            Si tu a faux tu recule de 8 cases!")
      print("                                            1- Hurluberlu")
      print("                                            2- soixiste")
      print("                                            3- Mirondale")
      w = int(input("                                      Veuillez choisir le numéro de la réponse:"))
      if w == 1:
         print("Bonne réponse!")
      else:
         print("Faux! Vous reculez de 8 cases!")

   elif B == 4:
      print("                                           le défis de Bowzer est le suivant: ")
      print("                                               Trouvez le mot qui existe:")
      print("                                            Si tu a faux tu recule de 8 cases!")
      print("                                            1- sordoive")
      print("                                            2- vésanine")
      print("                                            3- Ubuesque")
      w = int(input("                                      Veuillez choisir le numéro de la réponse:"))
      if w == 3:
         print("Bonne réponse!")
      else:
         print("Faux! Vous reculez de 8 cases!")

def ennigme_D():
   print("                                      ", "Vous êtes tombés sur l'ennemi: Dracula!")
   print("                                           le défis de Dracula est le suivant: ")
   print("                                            Lequel de ces métiers n'existe pas ou n'existe plus:")
   print("                                            Si tu a faux tu recule de 12 cases!")
   B = randint(1, 4)
   if B == 1:
      print("                                      1- pleureur profesionnel")
      print("                                      2- pousseur de passager de métro")
      print("                                      3- Babyssitter pour Autruche")
      print("                                      4- Chirurgien spécialiste de la téléchirurgie (chirurgie à distance)")
      w = int(input("                                      Veuillez choisir le numéro de la réponse:"))
      if w == 4:
         print("Bonne réponse!")
      else:
         print("Faux! Vous reculez de 12 cases!")
   elif B == 2:
      print("                                      1- Pilote de vols commerciaux vers l'espace.")
      print("                                      2- Testeur de déodorant")
      print("                                      3- cacheur de plaque d'immatriculation")
      w = int(input("                                      Veuillez choisir le numéro de la réponse:"))
      if w == 1:
         print("Bonne réponse!")
      else:
         print("Faux! Vous reculez de 12 cases!")
   elif B == 3:
      print("                                      1- Panda-Sitter")
      print("                                      2- Testeur de toboggans")
      print("                                      3- Réveilleur")
      w = int(input("                                      Veuillez choisir le numéro de la réponse:"))
      if w == 3:
         print("Bonne réponse!")
      else:
         print("Faux! Vous reculez de 12 cases!")
   else:
      print("                                      1- pécheur de vélo")
      print("                                      2- attrapeur de rats")
      print("                                      3- Gardien d'île")
      print("                                      4- électrocuteur de personne îvre")
      w = int(input("                                      Veuillez choisir le numéro de la réponse:"))
      if w == 2:
         print("Bonne réponse!")
      else:
         print("Faux! Vous reculez de 12 cases!")


def random_coord_ligne_ennemi(nb_lignes):
   coord_ennemi_ligne = randint(0, nb_lignes)
   print("coord_ennemi_ligne, ", coord_ennemi_ligne)
   return coord_ennemi_ligne

def random_coord_colonne_ennemi(nb_colonnes):
   coord_ennemi_colonne = randint(0, nb_colonnes)
   print("coord_ennemi_colonne ", coord_ennemi_colonne)
   return coord_ennemi_colonne

def insere_ennemi(coord_ligne, coord_colonne, tableau):
   tableau[coord_ligne][coord_colonne] = "X"

def game_winner(coord_arriv_ligne, coord_arriv_colonne, tableau):
   if tableau[coord_arriv_colonne][coord_arriv_ligne] == personnage:
      print("Vous avez GAGNER!")
      return True
   else:
      return False

def intersection_personnage_ennemi(coord_ennemi_ligne, coord_ennemi_colonne, tableau):
   print("intersection ")
   if personnage == tableau[coord_ennemi_ligne][coord_ennemi_colonne]:
      print("waaaaaaaaaaaw ")
      tableau[coord_ennemi_ligne][coord_ennemi_colonne] = "A"
      return True
   else:
      return False
      #ennigme_A()
   #if personnage == tableau[o][u] and tableau[o][u]!=tableau[i][r] and tableau[o][u]!=tableau[k][z]:
      #tableau[o][u] = "B"
   #if personnage == tableau[k][z] and tableau[k][z]!=tableau[i][r] and tableau[k][z]!=tableau[o][u]:
      #tableau[k][z] = "D"
'''
def move():
   d = input("Veuillez saisir dee pour lancer le dée:")
   if d == "dee":
      dee = 6 #randint(1, 6)
      print("Vous avez le droit de bouger votre personnage",dee, "fois dans le jeu! Choisissez bien!")

      ennemi = "B"
      p = 5
      q = 5
      r = 0
      c = 0
      x = 0
      while r<dee:
         if keyboard.read_key() == "8":
            print("\n")
            c +=1

         elif keyboard.read_key() == "2":
            print("\n")
            c -=1

         elif keyboard.read_key() == "6":
            print("\n")
            x +=1

         elif keyboard.read_key() == "4":
            print("\n")
            x -=1
         else:
            print("veuillez selectionner un touche entre (l-> left, r->right,u->up,d->down)")
         for i in range(lignes):
            a = []
            for j in range(colonnes):
               if j == (colonnes-1)+x and i == (lignes-1)-c:
                  a.append(personnage)
               #if personnage. == p and i == q:
                  #a.append(ennemi)
               else:
                  a.append("X")
            print(a)
         print(personnage)
         r +=1'''
   # print les propositions de déplacement
   # recupérer le choix de l'utilisateur
   # En fonction du choix appeler une fonctionnalité
   # Il faut une largeur que l'utilisateur definit -> pour monter et descendre largeur=position -largeur ou +largeur +prévoir les cas spécifique