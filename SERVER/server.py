import zmq
import time
from lobby import Lobby
from player_data import Player

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    lobby = Lobby()

    while True:
        message = socket.recv_string()
        print(f"Received request: {message}")

        response = ""

        parts = message.split(" ")
        if len(parts) >= 3 and parts[0] == "create_room":
            response = lobby.create_room(parts[1])

        elif len(parts) >= 4 and parts[0] == "join_room":
            player = Player(parts[3])
            response = lobby.join_room(parts[1], player)

        elif len(parts) >= 2 and parts[0] == "get_players":
            if parts[1] in lobby.rooms:
                room = lobby.rooms[parts[1]]
                response = ", ".join(room.get_players())

        socket.send_string(response)

if __name__ == "__main__":
    main()