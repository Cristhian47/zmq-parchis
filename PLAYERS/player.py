import zmq
from client_connection import connection
from client_menu import principal_menu

if __name__ == "__main__":
    socket = connection()
    principal_menu(socket)