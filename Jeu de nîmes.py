joueur1_baton = 0
joueur2_baton = 0

nombre_max_baton = 21

nom_joueur_1=input("Quel est le nom du joueur 1?")
nom_joueur_2=input("Quel est le nom du joueur 2?")

while nombre_max_baton > 0:
  joueur1_baton = input("nombre de baton que vous voulez retirer:")
  joueur1_baton = int(joueur1_baton)

  while joueur1_baton > 3:
    # SA veut que le nombre de baton du jouer 1 est supérieur à 3
    joueur1_baton = int(input("choisir un nombre inférieur ou égal à 3: "))


  nombre_max_baton = nombre_max_baton - joueur1_baton
  if nombre_max_baton <= 0:
    print(nom_joueur_2,"à gagné !!!!!")
    break

  print("il reste {} baton".format(nombre_max_baton))


  joueur2_baton = input("nombre de baton que vous voulez retirer:")
  joueur2_baton = int(joueur2_baton)
  
  while joueur2_baton > 3:
    joueur2_baton = int(input("choisir un nombre inférieur ou égal à 3: "))

  nombre_max_baton = nombre_max_baton - joueur2_baton
  if nombre_max_baton <= 0:
    print(nom_joueur_2,"à gagné !!!!!")
    break
  print("il reste {} baton".format(nombre_max_baton))
