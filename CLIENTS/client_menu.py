import zmq
import os
import time
from client_information import *
from client_game_menu import menu_board
from client_connection_brodcast import connection_brodcast

def lanzar_dados(self):
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
                    elif information[0] == "game_not_found":
                        time.sleep(2)
                        os.system("cls")
                        break
                
        elif opcion == "3":
            socket.send(b"exit")
            socket.close()
            print("exit")
            break
        