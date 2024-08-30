from motor_controller import MotorController

def evacuationJourney(motor_controller):
    
    print("Iniciando el viaje de evacuación")
    motor_controller.move_forward(duration=2)
    motor_controller.turn_left(duration=1)
    motor_controller.move_forward(duration=2)
    motor_controller.turn_right(duration=1)
    motor_controller.move_backward(duration=2)
    print("Viaje de evacuación completo")

# Uso de ejemplo
if __name__ == "__main__":
    motor_controller = MotorController(left_pin=12, right_pin=16)
    try:
        evacuationJourney(motor_controller)
    finally:
        motor_controller.cleanup()
