import socket

def send_evacuation_signal(robot_ip, port=9999):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((robot_ip, port))
    client.sendall("EVACUAR".encode())
    client.close()

if __name__ == "__main__":
    robot_ip = "192.168.100.157"
    send_evacuation_signal(robot_ip)
