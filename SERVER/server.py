import zmq
from server_connection import connection
from server_process_request import *

games = {}

if __name__=="__main__":
    socket1 = connection()
    print("Server running...")
    while True:
        message = socket1.recv_string()
        response = process_request(message)
        socket1.send(response.encode("utf-8"))
        print("Response:", response)