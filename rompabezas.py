import os
from os import system
from termcolor import colored

data = []

def main():
    
    print("BIENVENIDO AL ROMPABEZAS 4000v8\n\nProfesiones disponibles\n1. Alquimia\n2. Joyería\n")

    intro()

    os.remove("temp.txt") 
    data.clear()

    print("\n¿Qué te gustaría hacer?\n\n1. Volver a empezar\n2. Finalizar")
    end = input("Opción: ")
    match end:
        case "1": main()
        case "2": return

def intro():
    prof = input("Elige tu profesión: ")
    
    match prof:
        case "1": alquimia()
        case "2": joyeria()
        case _: 
            print("Parece que no te sabes los números. No te preocupes, lo volvemos a intentar")
            intro()



def alquimia():
    print("\nBienvenido al módulo de ALQUIMIA\n\nHaz click derecho para pegar tus datos")
    print(colored("Cuando termines, presiona ENTER dos veces\n\n","yellow"))
    
    input_data2()
    read_data()

    #elemT2, elemT3, omnium, primal, vial, agitating, tepid, frost, hochen, focus, saxi
    pocion(data[2], data[3], data[4], data[1], data[0], data[5])
    vers(data[7], data[8], data[6])
    focus(data[7], data[4], data[8], data[10], data[9], data[5])


def pocion(omnium, primal, vial, elem_t3, elem_t2, agitating):
    cost = 0.9*(3*omnium + primal + 5*vial)
    rev = 0.95*(0.75*elem_t3 + 0.25*elem_t2)*7.6
    cat = False

    if agitating/cost < 0.07:
        cost += agitating
        rev = 0.95*(0.8*elem_t3 + 0.2*elem_t2)*8
        cat = True

    profit = rev - cost

    text_color = profit_color(profit)
    catalizer_color = cat_color(cat)
    print(f"\nEl beneficio medio por fabricación de POCIÓN ELEMENTAL es de", colored(int(profit),text_color), "de oro con catalizador en", colored(cat,catalizer_color))


def vers(frost, hochen, tepid):
    cost = 0.9*(2*frost + 8 + 16*hochen)
    rev = 0.95*3*tepid
    profit = rev - cost

    text_color = profit_color(profit)
    print(f"\nEl beneficio medio por fabricación de AMPOLLA DE VERSATILIDAD es de", colored(int(profit),text_color), f"de oro")

def focus(frost, vial, hochen, saxi, focus, agitating):
    cost = 0.9*(frost + 5*vial + 20*hochen + 8*saxi)
    rev = 0.95*7.6*0.3*focus
    cat = False

    if agitating/cost < 0.07:
        cost+=agitating
        rev = 0.95*8*0.3*focus
        cat = True
    
    profit = rev - cost

    text_color = profit_color(profit)
    catalizer_color = cat_color(cat)
    print(f"\nEl beneficio medio por fabricación de POCIÓN DE ENFOQUE es de", colored(int(profit),text_color), "de oro con catalizador en", colored(cat,catalizer_color))


def joyeria():
    print("\nBienvenido al módulo de JOYERÍA\n\nHaz click derecho para pegar tus datos")
    print(colored("Cuando termines, presiona ENTER, CTRL+Z, ENTER\n\n","yellow"))
    
    input_data2()
    read_data()

    #engasteT2, engasteT3, polvo, diamante, serevita, orden, ambar, cinto, vial, fuego, tapon, paño
    engastes(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[11])
    viales(data[8], data[9], data[10], data[2])

def engastes(engaste_t2, engaste_t3, polvo, diamante, serevita, orden, ambar, cinto, paño):
    engaste = (engaste_t2 + engaste_t3)/2

    profit = 0.95*(engaste + 26*polvo + 0.3*diamante) - 0.9*(200*serevita + orden + 1.8) - paño
    prospectar = profit

    text_color = profit_color(profit)
    print(f"\nEl beneficio medio por fabricación de engastes PROSPECTANDO es de", colored(int(profit),text_color), f"de oro")

    profit = 0.95*engaste - 0.9*(12*polvo + orden + 20*ambar + cinto) - paño
    comprar = profit

    text_color = profit_color(profit)
    print(f"El beneficio medio por fabricación de engastes COMPRANDO es de", colored(int(profit),text_color), f"de oro\n")

    if(prospectar > 0 and comprar > 0):
        ratio = prospectar/comprar
        if ratio > 5:
            print("Parece que ahora mismo la opción más recomendable es PROSPECTAR")
        else:
            print("Parece que la opción más recomendable ahora mismo es COMPRAR")

def viales(vial, fuego, tapon, polvo):
    profit = 0.95*6*vial - 0.95*(fuego + 5*tapon + polvo + 0.2)

    text_color = profit_color(profit)
    print(f"\nEl beneficio medio por fabricación de viales es de", colored(int(profit),text_color), f"de oro")


def profit_color(var):
    if var >= 0:
        return "light_green"
    else:
        return "light_red"
    
def cat_color(var):
    if var:
        return "light_green"
    else:
        return "light_red"

def input_data():
    system("TYPE CON > temp.txt")

def input_data2():
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    text = '\n'.join(lines)

    with open("temp.txt", 'w') as file:
        file.write(text)

def read_data():
    with open("temp.txt", 'r') as file:
        next(file)

        for line in file:
            values = line.split(',')
            
            # Get the first value from the list
            first_value = values[0].strip()  # strip() removes leading/trailing whitespace

            data.append(float(int(first_value)/10000))

main()