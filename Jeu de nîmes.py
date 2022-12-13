joueur1_baton = 0
joueur2_baton = 0
joueur3_baton = 0
nombre_max_baton = 21

nom_joueur_1=input("Quel est le nom du joueur 1?")
nom_joueur_2=input("Quel est le nom du joueur 2?")
nom_joueur_3=input("Quel est le nom du joueur 3?")

while nombre_max_baton > 0:
  joueur1_baton = input(nom_joueur_1,"nombre de baton que vous voulez retirer:")
  joueur1_baton = int(joueur1_baton)

  while joueur1_baton > 3:
    # SA veut que le nombre de baton du jouer 1 est supérieur à 3
    joueur1_baton = int(input("choisir un nombre inférieur à 3: "))

  nombre_max_baton = nombre_max_baton - joueur1_baton
  if nombre_max_baton <= 0:
    print("Joueur1 à gagné !!!!!")
    break

  print("il reste {} baton".format(nombre_max_baton))

  joueur2_baton = input(nom_joueur_2,"nombre de baton que vous voulez retirer:")
  joueur2_baton = int(joueur2_baton)
  while joueur2_baton > 3:
    joueur2_baton = int(input("choisir un nombre inférieur à 3: "))

  nombre_max_baton = nombre_max_baton - joueur2_baton
  if nombre_max_baton <= 0:
    print("Joueur2 à gagné !!!!!")
    break
  print("il reste {} baton".format(nombre_max_baton))

  joueur3_baton = int(
    input(nom_joueur_2,"nombre de baton que vous voulez retirer:"))
  while joueur3_baton > 3:
    joueur3_baton = int(input("choisir un nombre inférieur à 3: "))

  nombre_max_baton = nombre_max_baton - joueur3_baton
  if nombre_max_baton <= 0:
    print("Joueur3 à gagné !!!!!")
    break
  print("il reste {} baton".format(nombre_max_baton))