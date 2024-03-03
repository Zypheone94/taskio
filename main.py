import os
from list_tasks import list_tasks
from read_task import read_task
from creating_task import creating_task

choise = str

while True:
    choise = input("Que voulez-vous faire ? \n"
                   "- Read (lire une de vos tâches). \n"
                   "- Modify (Créer ou modifier une de vos tâches). \n"
                   "- End (Mettre fin au programme). \n")
    if choise.lower() != 'read' or choise.lower() != 'modify' or choise.lower() != 'end':
        break
    else:
        print("Je n'ai pas compris votre demande.")

if choise.lower() == 'read':
    list_tasks()
    task_to_read = input("Quelle liste voulez-vous lire ? (end pour finir) : ")
    if task_to_read == 'end':
        print("Merci d'avoir utilisé Taskio !")
        exit()
    else:
        if not os.path.exists('tasks_list/' + task_to_read.replace(' ', '_') + '.txt'):
            print("Je n'ai pas trouvez votre liste.")
            print('tasks_list/' + task_to_read.replace(' ', '_') + '.txt')
            print("Merci d'avoir utilisé Taskio !")
            exit()
        else:
            read_task('tasks_list/' + task_to_read.replace(' ', '_') + '.txt')

elif choise.lower() == 'modify':
    creating_task()