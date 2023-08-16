import zmq
from player_connection import connection

def principal_menu(socket):
    while True:
            print("\nOptions :")
            print("1. Create Room")
            print("2. Join Room")
            print("3. Get Players")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                identifier = input("Enter room identifier: ")
                socket.send_string(f"create_room {identifier}")
                response = socket.recv_string()
                print(response)

            elif choice == "2":
                identifier = input("Enter room identifier: ")
                name = input("Enter your name: ")
                socket.send_string(f"join_room {identifier} {name}")
                response = socket.recv_string()
                print(response)

            elif choice == "3":
                identifier = input("Enter room identifier: ")
                socket.send_string(f"get_players {identifier}")
                response = socket.recv_string()
                print(f"Players in room: {response}")

            elif choice == "4":
                break

            else:
                print("Invalid choice")