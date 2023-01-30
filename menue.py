# Afficher les options du menu
# demander à l'utilisateur
# en fonction du choix appeler une des 4 fonctions du dessous

def Menu():
    print("Bienvenue sur le jeu Mario")
    print("Le but du jeu est de réussir à arriver sur le premier X, c'est-à-dire celui qui est tout en haut à gauche!")
    print("Vous allez tombés certaines fois sur des ennemis, qui vont vous lancer des énigmes, il faudra répondre juste!")
    print("Sinon vous serez contraint de revenir au point de départ!")
    print("commencer le jeu - A")
    c = input("Veuillez saisir A pour commencer le jeu:")
    if c := "A":
        tableau = []
        nb_lignes = 4
        nb_colonnes = 4
        player_coord_ligne = nb_lignes-1
        player_coord_colonne = nb_colonnes-1
        from start_game import random_coord_ligne_ennemi
        coord_ennemi_ligne = random_coord_ligne_ennemi(nb_lignes - 1)
        from start_game import random_coord_colonne_ennemi
        coord_ennemi_colonne = random_coord_colonne_ennemi(nb_colonnes - 1)
        from start_game import start_game
        #from start_game import move
        start_game()
        from start_game import initialise_game
        initialise_game(nb_lignes, nb_colonnes, tableau)
        from start_game import position_depart_personnage
        position_depart_personnage(nb_lignes-1, nb_colonnes-1, tableau)
        from start_game import affiche_tableau
        print("player_coord_ligne : ", player_coord_ligne)
        print("player_coord_colonne : ", player_coord_colonne)
        affiche_tableau(nb_lignes, nb_colonnes, tableau)

        #from start_game import insere_personnage
        #insere_personnage(4, 2, tableau)
        from start_game import move_player
        while True:
            from start_game import game_winner
            if game_winner(0, 0, tableau) == True:
                return
            from start_game import key_move_player
            print("Veuillez saisir soit(8 pour aller en haut,6 pour aller droite,4 pour aller à gauche,2 en bas): \n")
            direction = input()
            # r += 1
            key_board_touch = key_move_player(direction)

            if key_board_touch == 8:
                player_coord_ligne = move_player(direction, player_coord_ligne, player_coord_colonne, nb_lignes, nb_colonnes, tableau)
            if key_board_touch == 2:
                player_coord_ligne = move_player(direction, player_coord_ligne, player_coord_colonne, nb_lignes, nb_colonnes, tableau)
            if key_board_touch == 6:
                player_coord_colonne = move_player(direction, player_coord_ligne, player_coord_colonne, nb_lignes, nb_colonnes, tableau)
            if key_board_touch == 4:
                player_coord_colonne = move_player(direction, player_coord_ligne, player_coord_colonne, nb_lignes, nb_colonnes, tableau)
            print("player_coord_ligne : ", player_coord_ligne)
            print("player_coord_colonne : ", player_coord_colonne)
            from start_game import intersection_personnage_ennemi
            from start_game import ennigme_A
            if intersection_personnage_ennemi(coord_ennemi_ligne, coord_ennemi_colonne, tableau) == True:
                affiche_tableau(nb_lignes, nb_colonnes, tableau)
                if ennigme_A(nb_lignes-1, nb_colonnes-1, tableau) == False:
                    player_coord_ligne = nb_lignes - 1
                    player_coord_colonne = nb_colonnes - 1
                    from start_game import insere_ennemi
                    insere_ennemi(coord_ennemi_ligne, coord_ennemi_colonne, tableau)
                    coord_ennemi_ligne = random_coord_ligne_ennemi(nb_lignes - 1)
                    coord_ennemi_colonne = random_coord_colonne_ennemi(nb_colonnes - 1)
                else:
                    position_depart_personnage(coord_ennemi_ligne, coord_ennemi_colonne, tableau)
                    coord_ennemi_ligne = random_coord_ligne_ennemi(nb_lignes - 1)
                    coord_ennemi_colonne = random_coord_colonne_ennemi(nb_colonnes - 1)

            affiche_tableau(nb_lignes, nb_colonnes, tableau)
        #move()
    else:
        input("erreur, veuillez selectionner une lettre entre(A,B,C,D)")

Menu()