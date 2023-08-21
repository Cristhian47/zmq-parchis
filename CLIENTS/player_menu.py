import zmq
from player_connection import connection

def lanzar_dados(self):
        input("Presiona Enter para lanzar los dados...")
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        print(f"Primer dado: {dado1}")
        print(f"Segundo dado: {dado2}")

        print("Elige cómo asignar los dados a las fichas:")
        print("1. Dado 1 a ficha y Dado 2 a otra ficha")
        print("2. Suma de los dados a una ficha")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            ficha1 = int(input("Selecciona el id de la primera ficha (1, 2, 3 o 4): "))
            ficha2 = int(input("Selecciona el id de la segunda ficha (1, 2, 3 o 4): "))
            print(f"Dado 1 asignado a ficha {ficha1}")
            print(f"Dado 2 asignado a ficha {ficha2}")
        elif opcion == "2":
            ficha = int(input("Selecciona el id de la ficha (1, 2, 3 o 4): "))
            suma_dados = dado1 + dado2
            print(f"Suma de los dados asignada a ficha {ficha}: {suma_dados}")
        else:
            print("Opción inválida")

def get_ip_address(socket):
    try:
        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)

        return ip_address
    except Exception as e:
        print("Error al obtener la dirección IP:", e)
        return None

def principal_menu(socket):
    
    ip = get_ip_address(socket)

    while True:
            print("\nOptions :")
            print("1. Create Room")
            print("2. Join Room")
            print("3. Get Players")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                socket.send_string(f"create_room id {ip}")
                response = socket.recv_string()
                print(response)
                lobby_menu(socket)

            elif choice == "2":
                identifier = input("Enter room identifier: ")
                socket.send_string(f"join_room {identifier} {ip}")
                response = socket.recv_string()
                print(response)
                lobby_menu(socket)

            elif choice == "3":
                identifier = input("Enter room identifier: ")
                socket.send_string(f"get_players {identifier} {ip}")
                response = socket.recv_string()
                print(f"Players in room: {response}")

            elif choice == "4":
                break

            else:
                print("Invalid choice")

def lobby_menu(socket):
     
     ip = get_ip_address(socket)

     while True:
            print("\nOptions :")
            print("1. Start Game")
            print("2. Get Players")
            print("3. Exit")
            
            choice = input("Enter your choice: ")

            if choice == "1":
                socket.send_string(f"start_game id {ip}")
                response = socket.recv_string()
                print(response)
            
            elif choice == "2":
                identifier = input("Enter room identifier: ")
                socket.send_string(f"get_players {identifier} {ip}")
                response = socket.recv_string()
                print(f"Players in room: {response}")

            elif choice == "3":
                return
     