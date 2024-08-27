import Jetson.GPIO as GPIO
import time

# Asignación de pines GPIO
IN1_motor1 = 26  # GPIO26 -> Pin 37 en Jetson
IN2_motor1 = 16  # GPIO16 -> Pin 36 en Jetson
IN3_motor2 = 19  # GPIO19 -> Pin 35 en Jetson
IN4_motor2 = 20  # GPIO20 -> Pin 38 en Jetson

# Configuración de los pines GPIO
GPIO.setmode(GPIO.BCM)  # Usar la numeración BCM para los pines
GPIO.setup(IN1_motor1, GPIO.OUT)
GPIO.setup(IN2_motor1, GPIO.OUT)
GPIO.setup(IN3_motor2, GPIO.OUT)
GPIO.setup(IN4_motor2, GPIO.OUT)

# Función para mover ambos motores hacia adelante
def move_both_motors_forward():
    GPIO.output(IN1_motor1, GPIO.HIGH)
    GPIO.output(IN2_motor1, GPIO.LOW)
    GPIO.output(IN3_motor2, GPIO.HIGH)
    GPIO.output(IN4_motor2, GPIO.LOW)

# Función para mover ambos motores hacia atrás
def move_both_motors_backward():
    GPIO.output(IN1_motor1, GPIO.LOW)
    GPIO.output(IN2_motor1, GPIO.HIGH)
    GPIO.output(IN3_motor2, GPIO.LOW)
    GPIO.output(IN4_motor2, GPIO.HIGH)

# Función para detener ambos motores
def stop_both_motors():
    GPIO.output(IN1_motor1, GPIO.LOW)
    GPIO.output(IN2_motor1, GPIO.LOW)
    GPIO.output(IN3_motor2, GPIO.LOW)
    GPIO.output(IN4_motor2, GPIO.LOW)

# Código de prueba para controlar ambos motores
try:
    print("Moviendo ambos motores hacia adelante.")
    move_both_motors_forward()
    time.sleep(2)  # Mover ambos motores por 2 segundos

    print("Deteniendo ambos motores.")
    stop_both_motors()
    time.sleep(2)  # Pausar por 2 segundos

    print("Moviendo ambos motores hacia atrás.")
    move_both_motors_backward()
    time.sleep(2)  # Mover ambos motores hacia atrás por 2 segundos

    print("Deteniendo ambos motores.")
    stop_both_motors()
    time.sleep(2)  # Pausar por 2 segundos

except KeyboardInterrupt:
    print("Programa interrumpido por el usuario.")
finally:
    stop_both_motors()  # Asegurarse de que ambos motores estén detenidos
    GPIO.cleanup()  # Limpiar configuración de GPIO
    print("GPIO limpio y terminado.")
