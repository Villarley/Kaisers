from jetson_sender import JetsonSender
from motor_control import MotorController
import subprocess  # Importa el módulo subprocess

class EvacuationProtocol:
    def __init__(self, motor_controller=None):
        self.jetson_sender = JetsonSender()
        if motor_controller is None:
            # Inicializa el controlador de motores con pines por defecto si no se proporciona uno
            self.motor_controller = MotorController(left_pin=12, right_pin=16)
        else:
            # Usa el controlador de motores proporcionado
            self.motor_controller = motor_controller

    def execute_protocol(self):
        print("Ejecutando protocolo de evacuación...")
        evacuation_instruction = "1"
        response = self.jetson_sender.send_instruction(evacuation_instruction)

        if response:
            print(f"Respuesta del ESP32: {response}")
        else:
            print("No se recibió respuesta del ESP32.")
    
    def perform_evacuation_journey(self):
        print("Iniciando el viaje de evacuación")
        try:
            self.motor_controller.move_forward(duration=2)
            self.motor_controller.turn_left(duration=1)
            self.motor_controller.move_forward(duration=2)
            self.motor_controller.turn_right(duration=1)
            self.motor_controller.move_backward(duration=2)
            print("Viaje de evacuación completo")
        finally:
            self.motor_controller.cleanup()

    def open_cheese(self):
        print("Abriendo Cheese para captura de video...")
        try:
            subprocess.run(["cheese"], check=True)
            print("Cheese se ha iniciado correctamente.")
        except subprocess.CalledProcessError as e:
            print(f"Error al intentar abrir Cheese: {e}")

    def execute(self):
        self.execute_protocol()
        self.perform_evacuation_journey()
        self.open_cheese()

# Uso de ejemplo
if __name__ == "__main__":
    # Puedes crear un controlador de motor externamente si es necesario
    # motor_controller = MotorController(left_pin=12, right_pin=16)
    # protocolo = EvacuationProtocol(motor_controller)

    # O simplemente dejar que `EvacuationProtocol` lo maneje internamente
    protocolo = EvacuationProtocol()
    protocolo.execute()
