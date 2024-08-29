import socket

class JetsonSender:
    def __init__(self, esp32_ip='192.168.43.77', esp32_port=80):
        self.esp32_ip = esp32_ip
        self.esp32_port = esp32_port
        self.client_socket = None

    def connect(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.esp32_ip, self.esp32_port))

    def send_instruction(self, instruction):
        print(instruction)
        try:
            if not self.client_socket:
                self.connect()
            
            self.client_socket.sendall((instruction + '\n').encode())
            response = self.client_socket.recv(1024).decode()
            return response

        except Exception as e:
            print(f"Error durante la comunicación con el ESP32: {e}")
            return None

        finally:
            if self.client_socket:
                self.client_socket.close()
                self.client_socket = None
