import random

produits = [
    {"name": "epee", "prix": 50},
    {"name": "bombe", "prix": 100},
    {"name": "potion", "prix": 30},
    {"name": "super potion", "prix": 150},
]

inventaire = []

class Personnage:
    def __init__(self,nom,classe,pv,force,xp,OR,lvl,defense):
        self.nom = nom
        self.classe = classe
        self.pv = pv
        self.force = force
        self.xp = xp
        self.OR = OR
        self.lvl = lvl
        self.defense = defense

    def attacked(self,x):
        self.pv -= x

class Enemy(Personnage):
    def __init__(self, nom, classe, pv, force, xp,OR, lvl, defense):
        super().__init__(nom, classe, pv, force, xp,OR, lvl, defense)

golum = Enemy(nom="Golum",classe="mage",pv=50,force=30,xp=100,OR=50,lvl=0,defense=20)
barone = Enemy(nom="la Barone",classe="guerrier",pv=100,force=25,xp=200,OR=100,lvl=0,defense=20)
ogre = Enemy(nom="un Ogre",classe="guerrier",pv=200,force=10,xp=250,OR=150,lvl=0,defense=5)

lesenemy = [golum,barone,ogre]

class Heros(Personnage):
    def __init__(self, nom, classe, pv, force, xp,OR, lvl, defense, inventaire,distance,lieu,event):
        super().__init__(nom, classe, pv, force, xp,OR, lvl, defense)
        self.inventaire = inventaire
        self.distance = distance
        self.lieu = lieu
        self.event = event

    def explorer(self):
        if self.lieu == "foret":
            self.distance += 1
            print("🎄 vous arrivez dans la foret vous avez parcourut "+str(self.distance)+" km 🎄")
            if random.randint(1, 3) == 1:
                self.event="combat"
                print("🔥 Malheureusement vous devez combatre ! 🔥")
                enemy = lesenemy[random.randint(0, 2)]
                print("attention vous etes tomber sur "+enemy.nom)
                while enemy.pv>0 and self.pv>0:
                    self.pv -= enemy.force
                    enemy.pv -= self.force
                    if self.pv <= 0 :
                        print("vous avez combatu et avez perdu contre "+enemy.nom+" il ne lui restais que "+ str(enemy.pv) +" hp")
                    elif enemy.pv <= 0 :
                        print("vous avez combatu et avez ganger contre "+enemy.nom+" il vous reste "+str(self.pv)+" hp")

            elif random.randint(1, 3) == 2:
                self.event="trouvaille"
                if random.randint(1, 3) == 1:
                    self.xp += 50
                    print("🔥 Vous avez trouver 50 xp !! 🔥")
                elif random.randint(1, 3) == 2:
                    self.OR += 100 
                    print("🥇 Vous avez trouver 100 pieces d'or 🥇")
                else :
                    inventaire.append(produits[random.randint(0, 3)])
                    print("🔥 vous avez trouver un object ! 🔥")
                    # self.inventaire += inventaire.
                    # self.inventaire = self.inventaire.append(produits[random.randint(0, 3)])
            else :
                self.event="rien du tout"
                print("vous n'avez rien trouver !!")

    def village(self):
        self.distance = 0
        self.lieu = "village"

    def dormir(self):
        if self.OR >= 10:
            self.pv=200
            print("vous avez reganer tout vos pv , pv actuel : " + str(self.pv) + " pv")
        else :
            print("vous n avez pas assez d or")

    def magasin(self):
        print("voici tout les produits : ")
        for x in produits :
            print(x["name"])
            print("")

# print(produits[0]["name"])

# choseclass = input("veuillez choisir entre mage , guerrier et archer ")
choseclass = "mage"

monHeros= Heros(nom="artus",classe=choseclass,pv=200,force=30,xp=0,OR=0,lvl=0,defense=20,inventaire=[],distance=0,lieu="foret",event="")

choix=""
actionvillage=""

while monHeros.pv>0:
    while choix != "village" :
        print("✨ Bienvenu vous arrivez dans la foret ✨")
        monHeros.explorer()
        choix=str(input("voulez vous explorer ou partir au village ? "))

    while choix != "foret" : 
        print("✨ Bienvenu au village ✨")
        monHeros.village()
        actionvillage = str(input("que voulez vous faire dormir ou regarder les produits ? "))
        if actionvillage == "dormir":
            monHeros.dormir()
        elif actionvillage == "produits":
            monHeros.magasin()

        choix=str(input("voulez vous aller dans la foret ou partir au village ? "))

    

    



