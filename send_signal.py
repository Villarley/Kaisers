import socket

def send_evacuation_signal(robot_ip, port=9999):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((robot_ip, port))
    client.sendall("EVACUAR".encode())
    client.close()

if __name__ == "__main__":
    robot_ip = "192.168.1.10"  # Reemplaza con la IP de tu Jetson Nano
    send_evacuation_signal(robot_ip)