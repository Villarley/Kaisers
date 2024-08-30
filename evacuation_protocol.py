from jetson_sender import JetsonSender
from motor_control import MotorController
import subprocess  # Importa el módulo subprocess

class EvacuationProtocol:
    def __init__(self):
        self.jetson_sender = JetsonSender()
        self.motor_controller = MotorController(left_pin=12, right_pin=16)  # Inicializa el controlador de motores con los pines apropiados

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
    protocolo = EvacuationProtocol()
    protocolo.execute()
