import Jetson.GPIO as GPIO
import time

# Asignación de pines GPIO según la configuración mencionada
IN1 = 26  # GPIO26 -> Pin 37 en Jetson
IN2 = 16  # GPIO16 -> Pin 36 en Jetson
IN3 = 19  # GPIO19 -> Pin 35 en Jetson
IN4 = 20  # GPIO20 -> Pin 38 en Jetson

# Configuración de los pines GPIO
GPIO.setmode(GPIO.BCM)  # Usar la numeración BCM para los pines
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Función para mover el Motor 1 hacia adelante
def move_motor1_forward():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)

# Función para mover el Motor 1 hacia atrás
def move_motor1_backward():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)


def move_both():
    print("hallo")
    move_motor1_forward()
    move_motor2_forward()
    time.sleep(2)
    stop_motor1()
    stop_motor2()
    time.sleep(2)
    move_motor1_backward()
    move_motor2_backward()
    time.sleep(2)
    stop_motor1()
    stop_motor2()
    time.sleep(2)
# Función para detener el Motor 1
def stop_motor1():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)

# Función para mover el Motor 2 hacia adelante
def move_motor2_forward():
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

# Función para mover el Motor 2 hacia atrás
def move_motor2_backward():
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

# Función para detener el Motor 2
def stop_motor2():
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

# Código de prueba para controlar los motores
try:
    while True:
        move_both()

except KeyboardInterrupt:
    print("Programa interrumpido por el usuario.")
finally:
    GPIO.cleanup()
    stop_motor1()
    stop_motor2()
    # Limpia los GPIO al finalizar
    print("GPIO limpio y terminado.")
