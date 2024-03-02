import os
from add_content import add_content

# Vérifier l'existance d'un dossier de tache
if not os.path.isdir('tasks_List'):
    os.mkdir('tasks_list')

# Verification de l'existance d'une tache :
check = True

while check:
    task_name = input("Quel est le nom de votre liste ? ")
    file_path = 'tasks_list/' + task_name + '.json'
    if task_name == '' :
        print('Le nom de votre liste contient une erreur')
    elif len(task_name) < 5:
        print('Le nom de votre liste est trop court')
    elif not os.path.exists(file_path):
        check = False
    else:
        print("Votre liste existe déjà, voulez-vous la modifier ? (Y/n) : ")

    add_content(f'tasks_list/{task_name.replace(' ', '_')}.txt')

