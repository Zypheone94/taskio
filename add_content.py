import json
import os


def add_content(file_name):
    f = open(file_name, 'a')

    while True:
        value = input("Que voulez-vous ajouter à votre liste ? (end pour arreter) : ")
        if value == 'end':
            break
        else:
            f.write(value + '\n')
    f.close()

    print("Merci d'avoir utilisé Taskio !")
    exit()