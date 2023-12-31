import os
import zmq
import threading
import time

game_ended = False
game_started = False
thread_end = False
game_finished = False

def recibir_mensajes(socket):
    global game_ended
    global game_started
    while True:
        events = socket.poll(100, zmq.POLLIN)
        if events == zmq.POLLIN:
            mensaje = socket.recv_string()
            print(f"{mensaje} enter any option to continue...")
            if mensaje == "game_ended":
                game_ended = True
                break
            if mensaje == "game_started":
                game_started = True
        elif thread_end == True:
            break
        elif game_finished == True:
            break



def menu_board(player, socket, socket_brodcast):
    global game_ended
    global thread_end
    global game_started
    global game_finished
    
    thread = threading.Thread(target=recibir_mensajes, args=(socket_brodcast,))
    thread.start()
    
    while True:
        print(f"GAME {str(player.game_id).upper()} - PLAYER {str(player.color).upper()}".center(50, "-"))
        print("1. Start_game")
        print("2. Exit")  
        opcion = input("Select an option: ")

        if game_ended == True:
            break
        elif game_started == True:
            os.system("cls")
            #aqui  va el juego
            game_finished = True
            break
        else:
            if opcion == "1":
                message = f"start_game {player.game_id} | {player.color}" 
                socket.send_string(message)
                information = socket.recv_string()
                if information == "game_started":
                    #aaqui va el juego
                    pass
                print(information)
                time.sleep(2)
            elif opcion == "2":
                message = f"exit_game {player.game_id} | {player.color}"
                socket.send_string(message)
                information = socket.recv_string()
                print(information)
                thread_end = True
                time.sleep(2)
                break
        os.system("cls")

    os.system("cls")
    thread.join()
    game_ended = False
    thread_end = False
    game_started = False
    game_finished = False

    return True

