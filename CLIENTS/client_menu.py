import random
import zmq
import os
import time
from client_information import *
from client_game_menu import menu_board
from client_connection_brodcast import connection_brodcast
tablero = {
    "host_partida": "",
    "id": 6123,
    "colores_disponibles": ["amarillo","azul","rojo","verde"],
    "seguros": [5,12,17,22,29,34,39,46,51,56,63,68],
    "turno": "amarillo",
    "amarillo":{
        "fichas": [
            {
                "id":1,
                "posicion": 0
            },
            {
                "id":2,
                "posicion": 0
            },
            {
                "id":3,
                "posicion": 0
            },
            {
                "id":4,
                "posicion": 0
            }
        ],
        "entrada_cielo": 68,
        "inicio": 5
    },
    "azul":{
        "fichas": [
            {
                "id":1,
                "posicion": 0
            },
            {
                "id":2,
                "posicion": 0
            },
            {
                "id":3,
                "posicion": 0
            },
            {
                "id":4,
                "posicion": 0
            }
        ],
        "entrada_cielo": 17,
        "inicio": 22
    },
    "rojo":{
        "fichas": [
            {
                "id":1,
                "posicion": 0
            },
            {
                "id":2,
                "posicion": 0
            },
            {
                "id":3,
                "posicion": 0
            },
            {
                "id":4,
                "posicion": 0
            }
        ],
        "entrada_cielo": 34,
        "inicio": 39
    },
    "verde":{
        "fichas": [
            {
                "id":1,
                "posicion": 0
            },
            {
                "id":2,
                "posicion": 0
            },
            {
                "id":3,
                "posicion": 0
            },
            {
                "id":4,
                "posicion": 0
            }
        ],
        "entrada_cielo": 51,
        "inicio": 56
    }
}
def imprimir_tablero(tablero):
    print("ID del juego:", tablero["id"])
    print("Turno:", tablero["turno"])
    
    for color, data in tablero.items():
        if color in ["host_partida", "id", "colores_disponibles", "seguros", "turno"]:
            continue
        
        print("\nFichas de color", color.capitalize())
        for ficha in data["fichas"]:
            print("Ficha", ficha["id"], "- Posición:", ficha["posicion"])

def lanzar_dados(tablero, color):
        input("Presiona Enter para lanzar los dados...")
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        print(f"Primer dado: {dado1}")
        print(f"Segundo dado: {dado2}")

        print("Elige cómo asignar los dados a las fichas:")
        print("1. Dado 1 a ficha y Dado 2 a otra ficha")
        print("2. Suma de los dados a una ficha")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ficha1 = int(input("Selecciona el id de la primera ficha (1, 2, 3 o 4): "))
            ficha2 = int(input("Selecciona el id de la segunda ficha (1, 2, 3 o 4): "))
            print(f"Dado 1 asignado a ficha {ficha1}")
            print(f"Dado 2 asignado a ficha {ficha2}")
        elif opcion == "2":
            ficha = int(input("Selecciona el id de la ficha (1, 2, 3 o 4): "))
            suma_dados = dado1 + dado2
            print(f"Suma de los dados asignada a ficha {ficha}: {suma_dados}")
        else:
            print("Opción inválida")

def mover_ficha(tablero, color, id_ficha, num):
    # Buscar el color y la ficha en el tablero
    if color in tablero and "fichas" in tablero[color]:
        fichas_color = tablero[color]["fichas"]
        for ficha in fichas_color:
            if ficha["id"] == id_ficha:
                ficha["posicion"] += num
                break

def is_turn(tablero, color):
    return tablero['turno'] == color

def menu(socket):
    while True:
        global player
        print("Welcome to the game")
        print("1. Create game")
        print("2. Join game")
        print("3. Exit")

        opcion = input("Select an option: ")

        if opcion == "1":
            socket.send(b"create_game")
            message = socket.recv_string()
            if message:
                print(message)
                information = message.split(" ")
                game_id, color, port_brodcast = information[3], information[11], information[-1]
                player = jugador(color, game_id, port_brodcast)
                time.sleep(3)
                os.system("cls")
                socket_brodcast = connection_brodcast(int(port_brodcast))
                menu_board(player, socket, socket_brodcast)

        elif opcion == "2":
            os.system("cls")
            while True:
                print("Ingrese el id de la partida a la que desea unirse")
                game_id = input("Game id: ")
                socket.send_string(f"join_game {game_id}")
                message = socket.recv_string()
                if message:
                    information = message.split(" ")
                    print(information[0])
                    if information[0] == "game_joined":
                        color, port_brodcast = information[6], information[-1]
                        player = jugador(color, game_id, port_brodcast)
                        time.sleep(3)
                        os.system("cls")
                        socket_brodcast = connection_brodcast(int(port_brodcast))
                        index = menu_board(player, socket, socket_brodcast)
                        if index:
                            break

                        if is_turn(tablero, color):
                            lanzar_dados(tablero, color)
                        else :
                            imprimir_tablero(tablero)
                            
                            
                    elif information[0] == "game_not_found":
                        time.sleep(2)
                        os.system("cls")
                        break
                
        elif opcion == "3":
            socket.send(b"exit")
            socket.close()
            print("exit")
            break
        