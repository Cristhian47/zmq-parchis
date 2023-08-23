import zmq
import os
import time
from client_information import *
from client_game_menu import menu_board
from client_connection_brodcast import connection_brodcast

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
        