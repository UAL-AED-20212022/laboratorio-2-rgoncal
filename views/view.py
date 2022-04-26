from itertools import count
from models.LinkedList import LinkedList


def main():
    lista_ligada = LinkedList()
    while True:
        try:
            comandos = input().split()
        except EOFError:
            return
        if comandos[0] == "RPI":
            RPI(comandos[1], lista_ligada)
        elif comandos[0] == "RPF":
            RPF(comandos[1], lista_ligada)
        elif comandos[0] == "RPDE":
            RPDE(comandos[2], comandos[1], lista_ligada)
        elif comandos[0] == "RPAE":
            RPAE(comandos[2], comandos[1], lista_ligada)
        elif comandos[0] == "RPII":
            RPII(comandos[1], int(comandos[2]), lista_ligada)
        elif comandos[0] == "VNE":
            VNE(lista_ligada)
        elif comandos[0] == "VP":
            VP(comandos[1], lista_ligada)
        elif comandos[0] == "EPE":
            EPE(lista_ligada)
        elif comandos[0] == "EUE":
            EUE(lista_ligada)
        elif comandos[0] == "EP":
            EP(comandos[1], lista_ligada)


def RPI(país, lista_ligada):
    lista_ligada.insert_at_start(país)
    lista_ligada.traverse_list()

def RPF(país, lista_ligada):
    lista_ligada.insert_at_end(país)
    lista_ligada.traverse_list()

def RPDE(pais_registado, pais_novo, lista_ligada):
    lista_ligada.insert_after_item(pais_registado, pais_novo)
    lista_ligada.traverse_list()

def RPAE(pais_novo, pais_registado, lista_ligada):
    lista_ligada.insert_before_item(pais_novo, pais_registado)
    lista_ligada.traverse_list()


def RPII(pais, indice, lista_ligada):
    lista_ligada.insert_at_index(indice, pais)
    lista_ligada.traverse_list()

def VNE(lista_ligada):
    contagem = lista_ligada.get_count()
    print(f"O número de elementos são {contagem}.")
    

def VP(país, lista_ligada):
    if lista_ligada.search_item(país) == True:
        print(f"O país {país} encontra-se na lista.")
    else:
        print(f"O País {país} não se encontra na lista.")

def EPE(lista_ligada):
    país = lista_ligada.start_node.item
    lista_ligada.delete_at_start()
    print(f"O país {país} foi eliminado da lista.")


def EUE(lista_ligada):
    país = lista_ligada.get_last_node()
    lista_ligada.delete_at_end()
    print(f"O país {país} foi eliminado da lista.")

def EP(país, lista_ligada):
    if lista_ligada.search_item(país) == True:
        lista_ligada.delete_element_by_value(país)
        print(f"O país {país} foi eliminado da lista")
    else:
        print(f"O país {país} não se encontra na lista")



    

    