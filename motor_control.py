import Jetson.GPIO as GPIO
import time

class MotorController:
    def __init__(self, left_pin, right_pin):
        self.left_pin = left_pin
        self.right_pin = right_pin

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.left_pin, GPIO.OUT)
        GPIO.setup(self.right_pin, GPIO.OUT)

    def move_forward(self, duration=1):
        print("Moviendo hacia adelante")
        GPIO.output(self.left_pin, GPIO.HIGH)
        GPIO.output(self.right_pin, GPIO.HIGH)
        time.sleep(duration)
        self.stop()

    def move_backward(self, duration=1):
        print("Moviendo hacia atrás")
        GPIO.output(self.left_pin, GPIO.LOW)
        GPIO.output(self.right_pin, GPIO.LOW)
        time.sleep(duration)
        self.stop()

    def turn_left(self, duration=0.5):
        print("Girando a la izquierda")
        GPIO.output(self.left_pin, GPIO.LOW)
        GPIO.output(self.right_pin, GPIO.HIGH)
        time.sleep(duration)
        self.stop()

    def turn_right(self, duration=0.5):
        print("Girando a la derecha")
        GPIO.output(self.left_pin, GPIO.HIGH)
        GPIO.output(self.right_pin, GPIO.LOW)
        time.sleep(duration)
        self.stop()

    def stop(self):
        print("Deteniendo motores")
        GPIO.output(self.left_pin, GPIO.LOW)
        GPIO.output(self.right_pin, GPIO.LOW)

    def cleanup(self):
        GPIO.cleanup()

# Uso de ejemplo
if __name__ == "__main__":
    motor_controller = MotorController(left_pin=12, right_pin=16)
    motor_controller.move_forward(duration=2)
    motor_controller.turn_left(duration=1)
    motor_controller.move_backward(duration=2)
    motor_controller.cleanup()
