import socket
from evacuation_protocol import EvacuationProtocol
from motor_control import MotorController

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

if __name__ == "__main__":
    motor_controller = MotorController(left_pin=12, right_pin=16)
    protocolo = EvacuationProtocol(motor_controller)
    listener = TCPListener()
    listener.listen(protocolo.execute)