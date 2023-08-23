import zmq
from client_connection import connection
from client_menu import menu

#funcion main

if __name__ == "__main__":
    socket = connection()
    menu(socket)

