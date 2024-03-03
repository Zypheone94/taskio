from read_task import read_task


def add_content(file_name):
    f = open(file_name, 'a')

    while True:
        value = input("Que voulez-vous ajouter à votre liste ? (end pour arreter) : ")
        if value == 'end':
            break
        else:
            f.write(value + '\n')
        read_task(file_name)
    f.close()

    print("Merci d'avoir utilisé Taskio !")
    exit()