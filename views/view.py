from models.LinkedList import LinkedList


def main():

    lista_ligada = LinkedList()
    while True:
        comandos = input().split()
        if comandos[0] == "RPI":
            RPI(comandos[1], lista_ligada)
        elif comandos[0] == "RPF":
            EPF(comandos[1], lista_ligada)
        elif comandos[0] == "RPDE":
            RPDE(comandos[1], comandos[2], lista_ligada)
        elif comandos[0] == "RPAE":
            RPAE(comandos[1], comandos[2], lista_ligada)
        elif comandos[0] == "RPI":
            RPI(comandos[1], comandos[2], lista_ligada)
        elif comandos[0] == "VNE":
            VNE(comandos[1], lista_ligada)
        elif comandos[0] == "VP":
            VP(comandos[1], lista_ligada)
        elif comandos[0] == "EPE":
            VP(lista_ligada)
        elif comandos[0] == "EUE":
            EUE(lista_ligada)
        elif comandos[0] == "EP":
            EP(comandos[1], lista_ligada)



def RPI(pais, lista_ligada):
    lista_ligada.insert_at_start(pais)
    lista_ligada.traverse_list()



    














lista_ligada.insert_at_start

    