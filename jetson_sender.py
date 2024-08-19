import socket

# Configurar los detalles del servidor
esp32_ip = '192.168.94.238'  # Reemplaza con la IP de tu ESP32
esp32_port = 80           # Debe coincidir con el puerto configurado en el ESP32

# Crear el socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((esp32_ip, esp32_port))

try:
    while True:
        # Leer la instrucción a enviar
        instruction = input("Escribe una instrucción para el ESP32: ")
        if instruction.lower() == 'exit':
            break

        # Enviar la instrucción
        client_socket.sendall((instruction + '\n').encode())

        # Recibir la respuesta
        response = client_socket.recv(1024).decode()
        print("Respuesta del ESP32:", response)

finally:
    # Cerrar la conexión
    client_socket.close()