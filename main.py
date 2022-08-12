import fileinput
import sys, os

def menuDisplay():
    print('=============================')
    print('= Menu de gestion des stocks =')
    print('=============================')
    print('1. Ajouter un nouvel article à l\'inventaire')
    print('2. Retirer un article de l\'inventaire')
    print('3. Mise à jour de l\'inventaire')
    print('4. Rechercher un article dans l\'inventaire')
    print('5. imprimer le rapport d\'inventaire')
    print('99. Quitter')
    CHOICE = int(input("Entrer votre hoix >>> "))
    menuSelection(CHOICE)

def menuSelection(CHOICE):
    if CHOICE == 1:
        addInventory()
    elif CHOICE == 2:
        removeInventory()
    elif CHOICE == 3:
        updateInventory()
    elif CHOICE == 4:
        searchInventory()
    elif CHOICE == 5:
        printInventory()
    elif CHOICE == 99:
        exit()

def addInventory():
    InventoryFile = open('inventaire.txt', 'a')
    print("Ajout de l'inventaire")
    print("================")
    item_description = input("Entrez le nom de l'élément: ")
    item_quantity = input("Entrez la quantité de l'article: ")
    InventoryFile.write(item_description + '\n')
    InventoryFile.write(item_quantity + '\n')
    InventoryFile.close()
    CHOICE = int(input('Entrer (98) pour Continuer ou (99) pour Quittert: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()
    
def removeInventory():
    print("Suppression de l'inventaire")
    print("==================")
    item_description = input("Entrez le nom de l'article à retirer de l'inventaire: ")

    file = fileinput.input('inventaire.txt', inplace=True)

    for line in file:
         if item_description in line:
             for i in range(1):
                 next(file, None)
         else:
             print(line.strip('\n'), end='\n')
    item_description
    CHOICE = int(input('Entrer (98) pour continuer ou (99) pour Quitter: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()

def updateInventory():
    print("Mise à jour de l'inventaire")
    print("==================")
    item_description = input('Entrez l\'élément à mettre à jour: ')
    item_quantity = int(input("Saisissez la quantité mise à jour. Saisir - pour moins: "))

    with open('inventaire.txt', 'r') as f:
        filedata = f.readlines()

    replace = ""
    line_number = 0
    count = 0
    f = open('inventaire.txt','r')
    file = f.read().split('\n')
    for i, line in enumerate(file):
        if item_description in line:
            for b in file[i+1:i+2]:
                value = int(b)
                change = value + (item_quantity)
                replace = b.replace(b, str(change))
                line_number = count
            count = i + 1      
    f.close()
    
    filedata[count] = replace + '\n'

    with open('inventaire.txt', 'w') as f:
        for line in filedata:
            f.write(line)
                                            
                
    CHOICE = int(input('Entrer (98) pour continuer ou (99) pour Quitter: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()

def searchInventory():
    print('Recherche dans l\'inventaire')
    print('============================')
    item_description = input('Entrez le nom de l\'élément: ')
    
    f = open('inventaire.txt', 'r')
    search = f.readlines()
    f.close
    for i, line in enumerate(search):
        if item_description in line:
            for b in search[i:i+1]:
                print('Element:     ', b, end='')
            for c in search[i+1:i+2]:
                print('Quantite: ', c, end='')
                print('----------')
        
    CHOICE = int(input('Entrer (98) pour Continuer ou (99) pour Quitter: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()
        
def printInventory():
    InventoryFile = open('inventaire.txt', 'r')
    item_description = InventoryFile.readline()
    print('Inventaire actuel')
    print('-----------------')
    while item_description != '':
        item_quantity = InventoryFile.readline()
        item_description = item_description.rstrip('\n')
        item_quantity = item_quantity.rstrip('\n')
        print('Element:     ', item_description)
        print('Quantite: ', item_quantity)
        print('----------')
        item_description = InventoryFile.readline()
    InventoryFile.close()

    CHOICE = int(input('Entrer (98) pour Continuer ou (99) pour Quitter: '))
    if CHOICE == 98:
            menuDisplay()
    else:
        exit()



if __name__ == '__main__':
    menuDisplay()

