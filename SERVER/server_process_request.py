import json
from server import games
from server_initialize_brodcast import initialize_brodcast

game_id = 0 # global variable
MAX_PLAYERS = 4

Boards = {}
Ports_brodcast = 5555


def create_game():
    global game_id
    global Ports_brodcast
    game_id += 1

    Ports_brodcast += 1

    with open("tablero.json", "r") as file:
        board = json.load(file)

    #Separar el color del jugador host
    available_colors = board["colores_disponibles"]
    color = available_colors.pop(0)
    board["colores_disponibles"] = available_colors
    board["host_partida"] = color

    #Crear puerto de broadcast
    port_brodcast = initialize_brodcast(Ports_brodcast)
    #Agregar a los tableros activos
    Boards[game_id] =[board, port_brodcast, Ports_brodcast]
    

    return f"game with id {game_id} created and you are the host -> {color} | port brodcast: {Ports_brodcast}"

def join_game(id_game):
    global Boards
    if id_game in Boards.keys():
        board = Boards[id_game][0]
        port_brodcast = Boards[id_game][2]
        available_colors = board["colores_disponibles"]
        if len(available_colors) > 0:
            color = available_colors.pop(0)
            board["colores_disponibles"] = available_colors
        else:
            return "game_full"
        return f"game_joined | your color is -> {color} | port brodcast {port_brodcast}"
    else:
        return "game_not_found"

def exit():
    return "Exit"

def exit_game(game_id, color):
    global Boards   
    if Boards[int(game_id)][0]["host_partida"] == color:
        #enviar brodcast a los jugadores para salirse de la partida
        brodcast = Boards[int(game_id)][1]
        brodcast.send_string("game_ended")
        del Boards[int(game_id)]
    elif Boards[int(game_id)][0]["host_partida"] != color:
        available_colors = Boards[int(game_id)][0]["colores_disponibles"]
        available_colors.append(color)
        Boards[int(game_id)][0]["colores_disponibles"] = available_colors
    return "exit game"

def start_game(game_id, color):
    global Boards
    jugadores = Boards[int(game_id)][0]["colores_disponibles"]

    if Boards[int(game_id)][0]["host_partida"] == color:
        if len(jugadores) < 3:
            return "game_started"
        else:
            return "game_not_started"
    

def process_request(message):
    information = message.split(" ")
    if information[0] == "create_game":
        response = create_game()
    elif information[0] == "join_game":
        response = join_game(int(information[1]))
    elif information[0] == "exit_game":
        response = exit_game(information[1], information[3])
    elif information[0] == "exit":
        response = exit()
    elif information[0] == "start_game":
        response = start_game(information[1], information[3])
    return response
