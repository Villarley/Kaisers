import Jetson.GPIO as GPIO
import time

# Asignación de pines GPIO para Motor 1
IN1_motor1 = 19  # GPIO19 -> Pin 35 en Jetson
IN2_motor1 = 26  # GPIO26 -> Pin 37 en Jetson

# Asignación de pines GPIO para Motor 2
IN3_motor2 = 20  # GPIO20 -> Pin 38 en Jetson
IN4_motor2 = 16  # GPIO16 -> Pin 36 en Jetson

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

# Función para detener el Motor 1
def stop_motor1():
    GPIO.output(IN1_motor1, GPIO.LOW)
    GPIO.output(IN2_motor1, GPIO.LOW)

# Función para mover el Motor 2 hacia adelante
def move_motor2_forward():
    GPIO.output(IN3_motor2, GPIO.HIGH)
    GPIO.output(IN4_motor2, GPIO.LOW)

# Función para detener el Motor 2
def stop_motor2():
    GPIO.output(IN3_motor2, GPIO.LOW)
    GPIO.output(IN4_motor2, GPIO.LOW)

# Código de prueba para controlar los motores de manera secuencial
try:
    while True:
        # Mover Motor 1 hacia adelante
        print("Moviendo Motor 1 hacia adelante.")
        move_motor1_forward()
        time.sleep(2)  # Mover Motor 1 por 2 segundos

        # Detener Motor 1
        print("Deteniendo Motor 1.")
        stop_motor1()
        time.sleep(2)  # Pausar por 2 segundos

        # Mover Motor 2 hacia adelante
        print("Moviendo Motor 2 hacia adelante.")
        move_motor2_forward()
        time.sleep(2)  # Mover Motor 2 por 2 segundos

        # Detener Motor 2
        print("Deteniendo Motor 2.")
        stop_motor2()
        time.sleep(2)  # Pausar por 2 segundos

except KeyboardInterrupt:
    print("Programa interrumpido por el usuario.")
finally:
    stop_motor1()  # Asegurarse de que el Motor 1 esté detenido
    stop_motor2()  # Asegurarse de que el Motor 2 esté detenido
    GPIO.cleanup()  # Limpiar configuración de GPIO
    print("GPIO limpio y terminado.")
