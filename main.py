from motor_control import MotorController
from evacuation_protocol import EvacuationProtocol
from tcp_listener import TCPListener

def main():
    # Inicializa el controlador de motores si quieres pasarlo manualmente
    # motor_controller = MotorController(left_pin=12, right_pin=16)
    
    # Crea una instancia del protocolo de evacuación
    # Si no pasas un motor_controller, se inicializará internamente
    protocolo = EvacuationProtocol()  # Usar `EvacuationProtocol(motor_controller)` si usas un controlador específico

    # Inicializa y ejecuta el listener de TCP
    listener = TCPListener()
    listener.listen(protocolo.execute)  # Esto llama a `protocolo.execute` cuando se recibe una señal

if __name__ == "__main__":
    main()
