import Jetson.GPIO as GPIO
import time

# Asignación de pines GPIO para el primer controlador
IN1_motor1 = 26  # GPIO26 -> Pin 37 en Jetson
IN2_motor1 = 16  # GPIO16 -> Pin 36 en Jetson

# Asignación de pines GPIO para el segundo controlador
IN3_motor2 = 19  # GPIO19 -> Pin 35 en Jetson
IN4_motor2 = 20  # GPIO20 -> Pin 38 en Jetson

# Configuración de los pines GPIO
GPIO.setmode(GPIO.BCM)  # Usar la numeración BCM para los pines
GPIO.setup(IN1_motor1, GPIO.OUT)
GPIO.setup(IN2_motor1, GPIO.OUT)
GPIO.setup(IN3_motor2, GPIO.OUT)
GPIO.setup(IN4_motor2, GPIO.OUT)

# Función para mover el Motor 1 hacia adelante
def move_motor1_forward():
    GPIO.output(IN1_motor1, GPIO.HIGH)
    GPIO.output(IN2_motor1, GPIO.LOW)

# Función para mover el Motor 1 hacia atrás
def move_motor1_backward():
    GPIO.output(IN1_motor1, GPIO.LOW)
    GPIO.output(IN2_motor1, GPIO.HIGH)

# Función para detener el Motor 1
def stop_motor1():
    GPIO.output(IN1_motor1, GPIO.LOW)
    GPIO.output(IN2_motor1, GPIO.LOW)

# Función para mover el Motor 2 hacia adelante
def move_motor2_forward():
    GPIO.output(IN3_motor2, GPIO.HIGH)
    GPIO.output(IN4_motor2, GPIO.LOW)

# Función para mover el Motor 2 hacia atrás
def move_motor2_backward():
    GPIO.output(IN3_motor2, GPIO.LOW)
    GPIO.output(IN4_motor2, GPIO.HIGH)

# Función para detener el Motor 2
def stop_motor2():
    GPIO.output(IN3_motor2, GPIO.LOW)
    GPIO.output(IN4_motor2, GPIO.LOW)

# Código de prueba para controlar los motores
try:
    while True:
        # Mover ambos motores hacia adelante
        move_motor1_forward()
        move_motor2_forward()
        print("Ambos motores moviéndose hacia adelante.")
        time.sleep(2)

        # Mover ambos motores hacia atrás
        move_motor1_backward()
        move_motor2_backward()
        print("Ambos motores moviéndose hacia atrás.")
        time.sleep(2)

        # Detener ambos motores
        stop_motor1()
        stop_motor2()
        print("Ambos motores detenidos.")
        time.sleep(2)

except KeyboardInterrupt:
    print("Programa interrumpido por el usuario.")
finally:
    # Detener ambos motores antes de limpiar GPIO
    stop_motor1()
    stop_motor2()
    GPIO.cleanup()
    print("GPIO limpio y terminado.")
