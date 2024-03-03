import os
from add_content import add_content
from list_tasks import list_tasks

# Vérification de la liste de tache et l'existance d'un dossier contenant nos listes
list_tasks()


def creating_task():
    # Verification de l'existance d'une tache :
    check = True

    while check:
        task_name = input("Quel est le nom de votre liste (end pour finir) ? ")
        if task_name == "end":
            print("Merci d'avoir utilisé Taskio !")
            break
        file_path = 'tasks_list/' + task_name + '.txt'
        if task_name == '' :
            print('Le nom de votre liste contient une erreur')
        elif len(task_name) < 5:
            print('Le nom de votre liste est trop court')
        elif not os.path.exists(file_path):
            check = False
        else:
            print("Votre liste existe déjà, voulez-vous la modifier ? (Y/n) : ")

        if check == False:
            add_content(f'tasks_list/{task_name.replace(' ', '_')}.txt')
            pass

