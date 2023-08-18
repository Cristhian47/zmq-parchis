import zmq
from player_connection import connection
from player_menu import principal_menu

if __name__ == "__main__":
    socket = connection()
    principal_menu(socket)