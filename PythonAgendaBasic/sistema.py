from lib.interface import *
from lib.arquivo import *
from lib.def_basic import *

from time import sleep

file_name = "date.txt"

if not fileExist(file_name):
    create_file(file_name)

while True:
    highlight("Menu Principal", color_blue())
    menu(["Ver pessoas cadastradas", "Cadastrar nova pessoa", "Sair do sistema"])
    answer = input_int("menu")
    if answer == 1:
        read_file(file_name)
        input(color_yellow() + "Enter para prosseguir" + color_reset())

    elif answer == 2:
        highlight("Novo Cadastro", color_blue())
        name = input_str("nome")
        age = input_int("idade")
        register(file_name, name, age)

    elif answer == 3:
        highlight("Bye", color_red())
        break
    else:
        print(line(10).center(30))
        print(f"{color_red()}Erro{color_reset()} digite algo entre 1 e 3".center(42))
        print(line(10).center(30))
