import zmq
import time
from main_menu import MainMenu
from player_data import Player
from id_generator import Identifier_Generator

def build_game_structure():
    game_structure = {
        "id": 6123,
        "seguros": [5, 12, 17, 22, 29, 34, 39, 46, 51, 56, 63, 68],
        "turno": "red",
        "amarillo": {
            "fichas": [
                {"id": 1, "posicion": 0},
                {"id": 2, "posicion": 0},
                {"id": 3, "posicion": 0},
                {"id": 4, "posicion": 0}
            ],
            "entrada_cielo": 68,
            "inicio": 5
        },
        "azul": {
            "fichas": [
                {"id": 1, "posicion": 0},
                {"id": 2, "posicion": 0},
                {"id": 3, "posicion": 0},
                {"id": 4, "posicion": 0}
            ],
            "entrada_cielo": 17,
            "inicio": 22
        },
        "rojo": {
            "fichas": [
                {"id": 1, "posicion": 0},
                {"id": 2, "posicion": 0},
                {"id": 3, "posicion": 0},
                {"id": 4, "posicion": 0}
            ],
            "entrada_cielo": 34,
            "inicio": 39
        },
        "verde": {
            "fichas": [
                {"id": 1, "posicion": 0},
                {"id": 2, "posicion": 0},
                {"id": 3, "posicion": 0},
                {"id": 4, "posicion": 0}
            ],
            "entrada_cielo": 51,
            "inicio": 56
        }
    }
    return game_structure

def create_room(parts, main_menu, identifier_generator):
    if parts[0] == "create_room":
        print("room created")
        room_id = identifier_generator.generate_random_identifier()
        print(room_id)
                
        if not (room_id in main_menu.rooms):
            response = main_menu.create_room(room_id)
            return response
        else:
            response = "this room already exists, try again"
            return response

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    main_menu = MainMenu()
    identifier_generator = Identifier_Generator()

    while True:
        message = socket.recv_string()
        print(f"Received request: {message}")

        response = ""

        parts = message.split(" ")
        
        response = create_room(parts, main_menu, identifier_generator)

        if parts[0] == "join_room":
            print("join to room")
            player = Player("", "", parts[2])
            if (parts[1] in main_menu.rooms):
                player.current_room = parts[1]
                response = main_menu.join_room(parts[1], player)
            else:
                response = "room not found, try again"

        if parts[0] == "get_players":
            if parts[1] in main_menu.rooms:
                print("get players")
                room = main_menu.rooms[parts[1]]
                response = ", ".join(room.get_players())

        socket.send_string(response)

if __name__ == "__main__":
    main()