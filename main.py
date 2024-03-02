maList = []

while True:
    value = input("Que voulez-vous ajouter à votre liste ? (end pour arreter)")
    if value == 'end' :
        break
    else :
        maList.append(value)

if len(maList):
    for element in maList:
        print(f'- {element}')
else:
    print("Votre liste est vide !")