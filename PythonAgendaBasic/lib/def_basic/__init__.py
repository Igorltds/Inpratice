from lib.interface import *


def menu(list):
    x = 0
    print("Selecione uma dessas opções: \n")
    for item in list:
        x += 1
        print(f"{color_blue()}{x}{color_reset()} - {item}.")


def input_int(variable_name):
    while True:
        try:
            nun_int = int(
                input(f"\ndigite um valor de {variable_name}:{color_green()}"))
        except:
            print(line(10).center(30))
            print(f"{color_red()}Erro{color_reset()} digite um valor de {variable_name} valido".center(42))
            print(line(10).center(30))
        else:
            print(color_reset())
            return nun_int


def input_str(variable_name):
    while True:
        try:
            txt_str = input(f"digite um {variable_name}: {color_green()}")

        except:
            print(line(10).center(30))
            print(f"{color_red()}Erro{color_reset()} digite algo valido".center(42))
            print(line(10).center(30))
        else:
            print(color_reset())
            return txt_str
