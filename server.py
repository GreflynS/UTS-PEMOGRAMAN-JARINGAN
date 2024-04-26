# import socket
# import random
# import threading

# def handle_client(server_socket, client_address, client_id):
#     COLORS_TRANSLATIONS = {
#         "Red": "Merah",
#         "Orange": "Oranye",
#         "Yellow": "Kuning",
#         "Green": "Hijau",
#         "Blue": "Biru",
#         "Purple": "Ungu",
#         "Pink": "Merah muda",
#         "Brown": "Cokelat",
#         "Black": "Hitam",
#         "White": "Putih"
#     }

#     while True:
#         color_en = random.choice(list(COLORS_TRANSLATIONS.keys()))
#         server_socket.sendto(color_en.encode(), client_address)

#         try:
#             server_socket.settimeout(10)
#             response, _ = server_socket.recvfrom(1024)
#             response = response.decode().strip().capitalize()
#             if response == COLORS_TRANSLATIONS[color_en]:
#                 feedback = "Correct! Score: 100"
#             else:
#                 feedback = "Incorrect! The color was {}.".format(COLORS_TRANSLATIONS[color_en])
#         except socket.timeout:
#             feedback = "Timeout! The color was {}.".format(COLORS_TRANSLATIONS[color_en])

#         if "Incorrect" in feedback or "Timeout" in feedback:
#             feedback += " Score: 0"

#         print("Client {} - {}".format(client_id, feedback))

# def main():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     HOST = 'localhost'
#     PORT = 12345
#     server_socket.bind((HOST, PORT))
#     print("Waiting for connections...")

#     client_id = 1
#     while True:
#         data, client_address = server_socket.recvfrom(1024)
#         print("Connected to client {} at: {}".format(client_id, client_address))
#         client_thread = threading.Thread(target=handle_client, args=(server_socket, client_address, client_id))
#         client_thread.start()
#         client_id += 1

# if __name__ == "__main__":
#     main()

# import socket
# import random
# import time

# # Kamus untuk menerjemahkan kata warna
# COLOR_TRANSLATION = {
#     "red": "merah",
#     "blue": "biru",
#     "green": "hijau",
#     "yellow": "kuning",
#     "orange": "jingga",
#     "purple": "ungu",
#     "pink": "merah muda",
#     "brown": "coklat",
#     "black": "hitam",
#     "white": "putih"
# }

# # Fungsi untuk mengirimkan pesan UDP
# def send_message(sock, address, message):
#     sock.sendto(message.encode(), address)

# # Fungsi untuk menerima pesan UDP
# def receive_message(sock):
#     data, address = sock.recvfrom(1024)
#     return data.decode(), address

# # Fungsi untuk memulai permainan
# def start_game(server_address, num_clients):
#     # Membuat socket UDP
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     server_socket.bind(server_address)
    
#     clients = set()

#     print("Server telah dimulai.")

#     # Memulai permainan
#     while True:
#         # Mengirim kata warna acak kepada semua klien yang terhubung
#         random_color = random.choice(list(COLOR_TRANSLATION.keys()))
#         for client_address in clients:
#             send_message(server_socket, client_address, random_color)

#         # Menerima jawaban dari klien
#         responses = {}
#         start_time = time.time()
#         while time.time() - start_time < 5:
#             try:
#                 data, address = receive_message(server_socket)
#                 responses[address] = data.lower()
#             except socket.timeout:
#                 break

#         # Memberikan nilai feedback kepada klien
#         for client_address, response in responses.items():
#             if response == COLOR_TRANSLATION[random_color]:
#                 send_message(server_socket, client_address, "100")
#             else:
#                 send_message(server_socket, client_address, "0")

#         # Menambahkan klien baru ke dalam set klien yang terhubung
#         while len(clients) < num_clients:
#             client_data, client_address = server_socket.recvfrom(1024)
#             clients.add(client_address)
#             print(f"Klien {client_address} terhubung.")
        
#         # Memberikan jeda selama 10 detik
#         time.sleep(10)

#     server_socket.close()

# # Menjalankan server
# if __name__ == "__main__":
#     server_address = ('localhost', 9999)  # Ganti dengan alamat dan port yang sesuai
#     num_clients = 10  # bisa di gannti dengan jumlah klien yang diinginkan
#     start_game(server_address, num_clients)

# import socket
# import random
# import time

# # Daftar kata warna dalam bahasa Inggris dan terjemahannya dalam bahasa Indonesia
# COLOR_TRANSLATION = {
#     "red": "merah",
#     "green": "hijau",
#     "blue": "biru",
#     "yellow": "kuning",
#     "orange": "jingga",
#     "purple": "ungu",
#     "pink": "merah muda",
#     "brown": "coklat",
#     "black": "hitam",
#     "white": "putih"
# }

# # Fungsi untuk mengirim pesan ke semua klien
# def send_to_all_clients(sock, message, clients):
#     for client_address in clients:
#         sock.sendto(message.encode(), client_address)

# # Fungsi untuk menerima pesan dari klien
# def receive_from_client(sock):
#     data, addr = sock.recvfrom(1024)
#     return data.decode(), addr

# # Fungsi utama
# def main():
#     # Inisialisasi socket UDP
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     server_address = ('localhost', 12345)
#     server_socket.bind(server_address)

#     # Daftar klien yang terhubung
#     clients = []

#     print("Waiting for clients...")

#     while True:
#         # Kirim kata warna acak ke semua klien setiap 10 detik
#         color = random.choice(list(COLOR_TRANSLATION.keys()))
#         send_to_all_clients(server_socket, color, clients)
#         print("Sent color:", color)

#         # Terima jawaban dari klien dalam waktu 5 detik
#         server_socket.settimeout(5)
#         try:
#             response, client_address = receive_from_client(server_socket)
#             response = response.lower()
#             expected_translation = COLOR_TRANSLATION[color]
#             if response == expected_translation:
#                 print("Correct! Score = 100", client_address)
#                 server_socket.sendto("100".encode(), client_address)
#             else:
#                 print("Incorrect! Score = 0", client_address)
#                 server_socket.sendto("0".encode(), client_address)
#         except socket.timeout:
#             print("No response from clients")

#         # Cek apakah ada klien baru yang ingin terhubung
#         try:
#             data, client_address = server_socket.recvfrom(1024)
#             if client_address not in clients:
#                 clients.append(client_address)
#                 print("New client connected:", client_address)
#         except socket.error:
#             pass

#         time.sleep(10)

# if __name__ == "__main__":
#     main()

import socket
import random
import time

# Daftar warna dlm b. Inggris dan terjemahan dlm b. Indonesia
COLOR_TRANSLATION = {
    "red": "merah",
    "green": "hijau",
    "blue": "biru",
    "yellow": "kuning",
    "orange": "jingga",
    "purple": "ungu",
    "pink": "merah muda",
    "brown": "coklat",
    "black": "hitam",
    "white": "putih"
}

# Fungsi untuk mengirim pesan ke semua klien
def send_to_all_clients(sock, message, clients):
    for client_address in clients:
        sock.sendto(message.encode(), client_address)

# Fungsi untuk menerima pesan dari klien
def receive_from_client(sock):
    data, addr = sock.recvfrom(1024)
    return data.decode(), addr

# Fungsi utama
def main():
    # Inisialisasi socket UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Daftar klien yang terhubung
    clients = {}

    print("Server started.")

    while True:
        # Kirim kata warna acak ke semua klien setiap 10 detik
        color = random.choice(list(COLOR_TRANSLATION.keys()))
        send_to_all_clients(server_socket, color, list(clients.keys()))
        print("Sent color:", color)

        # Terima jawaban dari klien dalam waktu 10 detik
        server_socket.settimeout(10)
        try:
            response, client_address = receive_from_client(server_socket)
            response = response.lower()
            expected_translation = COLOR_TRANSLATION[color]
            if response == expected_translation:
                print("Correct answer from client", client_address)
                server_socket.sendto("100".encode(), client_address)
            else:
                print("Incorrect answer from client", client_address)
                server_socket.sendto("0".encode(), client_address)
        except socket.timeout:
            print("No response from clients")

        # Cek apakah ada klien baru yang ingin terhubung
        try:
            data, client_address = server_socket.recvfrom(1024)
            if client_address not in clients:
                clients[client_address] = True
                print("New client connected:", client_address)
        except socket.error:
            pass

        time.sleep(10)

if __name__ == "__main__":
    main()
