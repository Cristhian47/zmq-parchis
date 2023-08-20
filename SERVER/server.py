import zmq
import time
from main_menu import MainMenu
from player_data import Player

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    main_menu = MainMenu()

    while True:
        message = socket.recv_string()
        print(f"Received request: {message}")

        response = ""

        parts = message.split(" ")
        if parts[0] == "create_room":
            print("room created")
            response = main_menu.create_room(parts[1])

        elif parts[0] == "join_room":
            print("join to room")
            player = Player("")
            response = main_menu.join_room(parts[1], player)

        elif parts[0] == "get_players":
            if parts[1] in main_menu.rooms:
                print("get players")
                room = main_menu.rooms[parts[1]]
                response = ", ".join(room.get_players())

        socket.send_string(response)

if __name__ == "__main__":
    main()