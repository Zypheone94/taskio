import os

# Vérifier l'existance d'un dossier de tache
if not os.path.isdir('tasks_List'):
    os.mkdir('tasks_list')

# Verification de l'existance d'une tache :
check = True

while check:
    task_name = input("Quel est le nom de votre liste ? ")
    file_path = 'tasks_list/' + task_name + '.json'
    if not os.path.exists(file_path):
        check = False
    else:
        print("Votre liste existe déjà, veuillez spécifier un autre nom !")


task_list = [task_name, []]

while True:
    value = input("Que voulez-vous ajouter à votre liste ? (end pour arreter)")
    if value == 'end' :
        break
    else :
        task_list[1].append(value)

