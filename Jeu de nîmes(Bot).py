from random import randint
joueur1_baton = 0
joueur2_baton = 0

nombre_max_baton = 21
print("Pour jouer avec une IA,il faut appeller le second joueur:''bot''")
nom_joueur_1=input("Quel est le nom du joueur 1?")
nom_joueur_2=input("Quel est le nom du joueur 2?")

if nom_joueur_2=="bot":
  while nombre_max_baton > 0:
    print("Nombre de baton que",nom_joueur_1,"veut retirer:")
    joueur1_baton = input()
    joueur1_baton = int(joueur1_baton)

    while joueur1_baton > 3:
    # SA veut que le nombre de baton du jouer 1 est supérieur à 3
      joueur1_baton = int(input("choisir un nombre inférieur ou égal à 3: "))


    nombre_max_baton = nombre_max_baton - joueur1_baton
    if nombre_max_baton <= 0:
      print(nom_joueur_1,"à gagné !!!!!")
      break
    
    print("il reste {} baton".format(nombre_max_baton))
    
    BOT_baton = randint(1, 4)
    BOT_baton = int(BOT_baton)

    nombre_max_baton = nombre_max_baton - BOT_baton
    if nombre_max_baton <= 0:
      print("BOT à gagné !!!!!")
      break
    print("BOT a pris {} baton".format(BOT_baton))
    print("il reste {} baton".format(nombre_max_baton))
else:
    while nombre_max_baton > 0:
      print("Nombre de baton que",nom_joueur_1,"veut retirer:")
      joueur1_baton = input()
      joueur1_baton = int(joueur1_baton)

      while joueur1_baton > 3:
    # SA veut que le nombre de baton du jouer 1 est supérieur à 3
        joueur1_baton = int(input("choisir un nombre inférieur ou égal à 3: "))

      nombre_max_baton = nombre_max_baton - joueur1_baton
      if nombre_max_baton <= 0:
        print(nom_joueur_1,"à gagné !!!!!")
        break
      print("il reste {} baton".format(nombre_max_baton))
      
      print("Nombre de baton que",nom_joueur_2,"veut retirer:")
      joueur2_baton = input()
      joueur2_baton = int(joueur2_baton)
  
      while joueur2_baton > 3:
        joueur2_baton = int(input("choisir un nombre inférieur à 3: "))

      nombre_max_baton = nombre_max_baton - joueur2_baton
      if nombre_max_baton <= 0:
          print(nom_joueur_2,"à gagné !!!!!")
          break
      print("il reste {} baton".format(nombre_max_baton))
      

    
   