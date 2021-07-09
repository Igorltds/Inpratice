from lib.interface import *


def fileExist(file_name):
    try:
        open(file_name, 'rt').close()

    except FileNotFoundError:
        return False
    else:
        return True


def create_file(file_name):
    try:
        open(file_name, "w+")
    except:
        print("Houve um erro na criação do arquivo")
    else:
        print(f"Arquivo {file_name} criado sucesso")


def read_file(file_name):
    try:
        file = open(file_name, "r")
    except:
        print(f"erro ao ler arquivo {file_name}")
    else:

        highlight("Pessoas Cadastradas", color_green())
        for linha in file:
            dado = linha.split(';')
            dado[0], dado[1] = dado[0].replace("\n",""), dado[1].replace("\n","")
            print(f"{dado[0]:<30} {dado[1]:>3} anos")

def register(file_name, personal_name="desconhecido", personal_age=0):
    try:
        a = open(file_name, "a")
    except:
        print("Houve um erro abertura do arquivo")
    else:
        try:
            a.write(f'{personal_name}; {personal_age}\n')
        except:
            print("houve um erro na hora de escrever os dados! ")
        else:
            print(f"Sucesso no cadastro de {personal_name}")
