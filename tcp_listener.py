import socket

class TCPListener:
    def __init__(self, host="0.0.0.0", port=9999):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(1)
        print(f"Esperando conexión en {host}:{port}...")

    def listen(self, callback):
        conn, addr = self.server.accept()
        print(f"Conexión recibida de {addr}")
        data = conn.recv(1024).decode()
        if data == "EVACUAR":
            print("Señal de evacuación recibida!")
            callback()
        conn.close()

# Uso de ejemplo
if __name__ == "__main__":
    def protocolo_evacuacion():
        print("Ejecutando protocolo de evacuación...")

    listener = TCPListener()
    listener.listen(protocolo_evacuacion)
