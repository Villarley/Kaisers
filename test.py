import Jetson.GPIO as GPIO
import time

# GPIO pin assignment for Motor 1 (same side as Motor 3)
IN1_motor1 = 19  # GPIO19 -> Pin 35 on Jetson
IN2_motor1 = 26  # GPIO26 -> Pin 37 on Jetson

# GPIO pin assignment for Motor 2
IN3_motor2 = 20  # GPIO20 -> Pin 38 on Jetson
IN4_motor2 = 16  # GPIO16 -> Pin 36 on Jetson

# GPIO pin assignment for Motor 3 (same side as Motor 1)
IN1_motor3 = 17  # GPIO17 -> Pin 11 on Jetson
IN2_motor3 = 27  # GPIO27 -> Pin 13 on Jetson

# GPIO pin assignment for Motor 4
IN3_motor4 = 22  # GPIO22 -> Pin 10 on Jetson
IN4_motor4 = 23  # GPIO23 -> Pin 12 on Jetson

# GPIO setup
GPIO.setmode(GPIO.BCM)  # Use BCM numbering for GPIO pins
GPIO.setup(IN1_motor1, GPIO.OUT)
GPIO.setup(IN2_motor1, GPIO.OUT)
GPIO.setup(IN3_motor2, GPIO.OUT)
GPIO.setup(IN4_motor2, GPIO.OUT)
GPIO.setup(IN1_motor3, GPIO.OUT)
GPIO.setup(IN2_motor3, GPIO.OUT)
GPIO.setup(IN3_motor4, GPIO.OUT)
GPIO.setup(IN4_motor4, GPIO.OUT)

# Function to move Motor 1 forward
def move_motor1_forward():
    print("Moving Motor 1 forward.")
    GPIO.output(IN1_motor1, GPIO.HIGH)
    GPIO.output(IN2_motor1, GPIO.LOW)

# Function to stop Motor 1
def stop_motor1():
    print("Stopping Motor 1.")
    GPIO.output(IN1_motor1, GPIO.LOW)
    GPIO.output(IN2_motor1, GPIO.LOW)

# Function to move Motor 2 forward
def move_motor2_forward():
    print("Moving Motor 2 forward.")
    GPIO.output(IN3_motor2, GPIO.HIGH)
    GPIO.output(IN4_motor2, GPIO.LOW)

# Function to stop Motor 2
def stop_motor2():
    print("Stopping Motor 2.")
    GPIO.output(IN3_motor2, GPIO.LOW)
    GPIO.output(IN4_motor2, GPIO.LOW)

# Function to move Motor 3 forward
def move_motor3_forward():
    print("Moving Motor 3 forward.")
    GPIO.output(IN1_motor3, GPIO.HIGH)
    GPIO.output(IN2_motor3, GPIO.LOW)

# Function to stop Motor 3
def stop_motor3():
    print("Stopping Motor 3.")
    GPIO.output(IN1_motor3, GPIO.LOW)
    GPIO.output(IN2_motor3, GPIO.LOW)

# Function to move Motor 4 forward
def move_motor4_forward():
    print("Moving Motor 4 forward.")
    GPIO.output(IN3_motor4, GPIO.HIGH)
    GPIO.output(IN4_motor4, GPIO.LOW)

# Function to stop Motor 4
def stop_motor4():
    print("Stopping Motor 4.")
    GPIO.output(IN3_motor4, GPIO.LOW)
    GPIO.output(IN4_motor4, GPIO.LOW)

# Function to move all motors forward
def move_all_forward():
    print("Moving all motors forward.")
    move_motor1_forward()
    move_motor2_forward()
    move_motor3_forward()
    move_motor4_forward()

# Function to stop all motors
def stop_all():
    print("Stopping all motors.")
    stop_motor1()
    stop_motor2()
    stop_motor3()
    stop_motor4()

# Function to turn 90 degrees using Motors 2 and 4 (opposite side of Motors 1 and 3)
def turn_90_degrees():
    print("Turning 90 degrees using Motors 2 and 4.")
    move_motor2_forward()  # Motors on the opposite side move to turn
    move_motor4_forward()
    stop_motor1()
    stop_motor3()
    time.sleep(1)  # Adjust time for accurate 90-degree turn
    stop_all()

# Test code to control the motors individually and perform a 90-degree turn
try:
    # Move Motor 1 forward
    move_motor1_forward()
    time.sleep(2)  # Move Motor 1 for 2 seconds
    stop_motor1()
    time.sleep(1)  # Pause for 1 second

    # Move Motor 2 forward
    move_motor2_forward()
    time.sleep(2)  # Move Motor 2 for 2 seconds
    stop_motor2()
    time.sleep(1)  # Pause for 1 second

    # Move Motor 3 forward
    move_motor3_forward()
    time.sleep(2)  # Move Motor 3 for 2 seconds
    stop_motor3()
    time.sleep(1)  # Pause for 1 second

    # Move Motor 4 forward
    move_motor4_forward()
    time.sleep(2)  # Move Motor 4 for 2 seconds
    stop_motor4()
    time.sleep(1)  # Pause for 1 second

    # Move all motors forward
    move_all_forward()
    time.sleep(2)  # Move all motors for 2 seconds
    stop_all()
    time.sleep(1)  # Pause for 1 second

    # Turn 90 degrees
    turn_90_degrees()
    time.sleep(2)  # Pause for 2 seconds after turn

except KeyboardInterrupt:
    print("Program interrupted by the user.")
finally:
    stop_all()  # Ensure all motors are stopped
    GPIO.cleanup()  # Clean up GPIO settings
    print("GPIO cleaned up and program terminated.")
