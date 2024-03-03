import os


def list_tasks():
    # Vérifier l'existance d'un dossier de tache
    if not os.path.isdir('tasks_List'):
        os.mkdir('tasks_list')
    else:
        tasks_list = os.listdir('tasks_List')
        for index, task in enumerate(tasks_list):
            print(f'- {index + 1} : {task}')