from jetson_sender import JetsonSender

class EvacuationProtocol:
    def __init__(self):
        self.jetson_sender = JetsonSender()

    def execute(self):
        print("Ejecutando protocolo de evacuación...")
        evacuation_instruction = "1"
        response = self.jetson_sender.send_instruction(evacuation_instruction)

        if response:
            print(f"Respuesta del ESP32: {response}")
        else:
            print("No se recibió respuesta del ESP32.")

# Uso de ejemplo
if __name__ == "__main__":
    protocolo = EvacuationProtocol()
    protocolo.execute()
