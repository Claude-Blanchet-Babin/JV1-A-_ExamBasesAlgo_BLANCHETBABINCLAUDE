#Partie 1 - Tri à bulles

#question 1

print("question 1")

myTable = [22,11,50,7,42]
i=""
j=""
print(myTable)
print("Quelle est la position de l'élément que vous souhaitez déplacer")
i=int (input())
print("Quelle est la position de l'élément avec lequel vous souhaitez l'échanger")
j=int (input())

save = myTable[i]
myTable[i]=myTable[j]
myTable[j]=save

print(myTable)

#question 2

print(" ")
print("question 2")

myTable = [22,11,50,7,42]

maxiValeur=0
maxiIndice=0

for i in range (0,len(myTable)):
    if (myTable[i]>maxiValeur):
        maxiValeur=myTable[i]
        maxiIndice=i

myTable.pop(maxiIndice)
myTable.append(maxiValeur)

print (myTable)

#question 3

print(" ")
print("question 3")

myTable = [11,22,50,7,42]

for j in range(0,len(myTable)):
    maxiValeur = 0
    maxiIndice = 0
    
    for i in range(j,len(myTable)):
        if (myTable[i]>maxiValeur):
            maxiValeur = myTable[i]
            maxiIndice = i
    print(" ")
    print(j + 1,"ème étape :")
    print(myTable)
    print("Le plus grand est",maxiValeur,"à la position",maxiIndice + 1)
    print("On insert le nombre à la position",j + 1,"et on supprime celui à la position",maxiIndice + 1)

    myTable.pop(maxiIndice) 
    myTable.insert(j,maxiValeur)
    
print(myTable)

#question 4

#Le tri à bulle est très lent car il est dépendant de la longueur de la liste
#En effet il est obligé de passer en revue l'intégralité de la liste pour définir quel est l'élement à déplacer
#Le temps d'exécution est donc proportionnel à la taille de la liste

#Partie 2 - Tic tac toe

#question 1

print(" ")
print("question 1")
print("afficher la grille de jeu")

#test d'une grille automatique
bloc = ""
for i in range(1,4):
    bloc += "[] "
    for n in range(0,i):
        print(bloc)
    print(" ")
#fin du test


#création d'une grille au format brut avec un tableau
tableauMorpion = [" "," "," "," "," "," "," "," "," ",]    

print("|1-",tableauMorpion[0],"|2-",tableauMorpion[1],'|3-',tableauMorpion[2],"|")
print("-------------------")
print("|4-",tableauMorpion[3],"|5-",tableauMorpion[4],'|6-',tableauMorpion[5],"|")
print("-------------------")
print("|7-",tableauMorpion[6],"|8-",tableauMorpion[7],'|9-',tableauMorpion[8],"|")
print(" ")

#question 2

print(" ")
print("question 2")
print("jouer un O ou un X")

joueur= 0
position = " "

if (joueur == 0):    
    position = int(input())
    tableauMorpion[position-1] = "X"
    joueur = 1
else :
    eposition = int(input())
    tableauMorpion[position-1] = "O"
    joueur = 0

#question 3

print(" ")
print("question 3")
print("vérifier si une ligne comporte 3 symboles identique")

victoire =False

if ( i >= 4 and (
    (tableauMorpion[0]==tableauMorpion[1]==tableauMorpion[2]!=" ") or (tableauMorpion[3]==tableauMorpion[4]==tableauMorpion[5]!=" ") or
    (tableauMorpion[6]==tableauMorpion[7]==tableauMorpion[8]!=" ") or (tableauMorpion[0]==tableauMorpion[4]==tableauMorpion[8]!=" ") or
    (tableauMorpion[6]==tableauMorpion[4]==tableauMorpion[2]!=" ") or (tableauMorpion[0]==tableauMorpion[3]==tableauMorpion[6]!=" ") or
    (tableauMorpion[1]==tableauMorpion[4]==tableauMorpion[7]!=" ") or (tableauMorpion[2]==tableauMorpion[5]==tableauMorpion[8]!=" "))):
    
    if (joueur == 0):
            print("Le joueur O gagne")
    else :
             print("Le joueur X gagne")
    victoire = True

#question 4

print(" ")
print("question 4")
print("Vérifier si la grille est complète")

#pour compléter la grille au complet, il faut imposer 9 tours de jeu avec un "for"
#si c'est 9 tour sont écoulés et qu'il n'y a aucune notification de victoire, cela signifie que la grille est complète et qu'il n'y a aucun vainqueur

#question 5

print(" ")
print("question 4")
print("Jouer à deux au Tic tac toe")

#assemblage du code

tableauMorpion = [" "," "," "," "," "," "," "," "," ",] 

for i in range (0,9):
  
    print("|1-",tableauMorpion[0],"|2-",tableauMorpion[1],'|3-',tableauMorpion[2],"|")
    print("-------------------")
    print("|4-",tableauMorpion[3],"|5-",tableauMorpion[4],'|6-',tableauMorpion[5],"|")
    print("-------------------")
    print("|7-",tableauMorpion[6],"|8-",tableauMorpion[7],'|9-',tableauMorpion[8],"|")
    print(" ")

    if (joueur == 0):    
        position = int(input())
        tableauMorpion[position-1] = "X"
        joueur = 1
    else :
        eposition = int(input())
        tableauMorpion[position-1] = "O"
        joueur = 0

    if ( i >= 4 and (
    (tableauMorpion[0]==tableauMorpion[1]==tableauMorpion[2]!=" ") or (tableauMorpion[3]==tableauMorpion[4]==tableauMorpion[5]!=" ") or
    (tableauMorpion[6]==tableauMorpion[7]==tableauMorpion[8]!=" ") or (tableauMorpion[0]==tableauMorpion[4]==tableauMorpion[8]!=" ") or
    (tableauMorpion[6]==tableauMorpion[4]==tableauMorpion[2]!=" ") or (tableauMorpion[0]==tableauMorpion[3]==tableauMorpion[6]!=" ") or
    (tableauMorpion[1]==tableauMorpion[4]==tableauMorpion[7]!=" ") or (tableauMorpion[2]==tableauMorpion[5]==tableauMorpion[8]!=" "))):
    
        if (joueur == 0):
                print("Le joueur O gagne")
        else :
                print("Le joueur X gagne")

#question 6

#programmer un jeu de puissance 4
#Pour la création d'un puissance 4 il est nécessaire de changer la taille de grille et de la faire correspondre avec un jeu de puissance 4
#Il faut faire en sorte qu'on ne puisse pas poser un nouveau jeton tant qu'il n'y a pas déjà un jeton en dessous
#(Sauf s'il s'agit de la première ligne)
#à la manière de la première tentative, automatisé la création du tableau permet de gagner du temps de codage
