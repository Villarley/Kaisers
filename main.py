from motor_control import MotorController
from evacuation_protocol import evacuationJourney
from tcp_listener import TCPListener

def main():
    # Inicializa el controlador de motores (aún no usado en este ejemplo)
    motor_controller = MotorController (left_pin=12, right_pin=16)

    # Inicializa el protocolo de evacuación
    protocolo = evacuationJourney()

    # Inicializa y ejecuta el listener
    listener = TCPListener()
    listener.listen(protocolo.execute)

if __name__ == "__main__":
    main()
