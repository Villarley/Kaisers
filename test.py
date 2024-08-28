import Jetson.GPIO as GPIO
import time

# GPIO pin assignment for Motor 1
IN1_motor1 = 19  # GPIO19 -> Pin 35 on Jetson
IN2_motor1 = 26  # GPIO26 -> Pin 37 on Jetson

# GPIO pin assignment for Motor 2
IN3_motor2 = 20  # GPIO20 -> Pin 38 on Jetson
IN4_motor2 = 16  # GPIO16 -> Pin 36 on Jetson

# GPIO pin assignment for Motor 3
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
    GPIO.output(IN1_motor1, GPIO.HIGH)
    GPIO.output(IN2_motor1, GPIO.LOW)

# Function to move Motor 1 backward
def move_motor1_backward():
    GPIO.output(IN1_motor1, GPIO.LOW)
    GPIO.output(IN2_motor1, GPIO.HIGH)

# Function to stop Motor 1
def stop_motor1():
    GPIO.output(IN1_motor1, GPIO.LOW)
    GPIO.output(IN2_motor1, GPIO.LOW)

# Function to move Motor 2 forward
def move_motor2_forward():
    GPIO.output(IN3_motor2, GPIO.HIGH)
    GPIO.output(IN4_motor2, GPIO.LOW)

# Function to move Motor 2 backward
def move_motor2_backward():
    GPIO.output(IN3_motor2, GPIO.LOW)
    GPIO.output(IN4_motor2, GPIO.HIGH)

# Function to stop Motor 2
def stop_motor2():
    GPIO.output(IN3_motor2, GPIO.LOW)
    GPIO.output(IN4_motor2, GPIO.LOW)

# Function to move Motor 3 forward
def move_motor3_forward():
    GPIO.output(IN1_motor3, GPIO.HIGH)
    GPIO.output(IN2_motor3, GPIO.LOW)

# Function to move Motor 3 backward
def move_motor3_backward():
    GPIO.output(IN1_motor3, GPIO.LOW)
    GPIO.output(IN2_motor3, GPIO.HIGH)

# Function to stop Motor 3
def stop_motor3():
    GPIO.output(IN1_motor3, GPIO.LOW)
    GPIO.output(IN2_motor3, GPIO.LOW)

# Function to move Motor 4 forward
def move_motor4_forward():
    GPIO.output(IN3_motor4, GPIO.HIGH)
    GPIO.output(IN4_motor4, GPIO.LOW)

# Function to move Motor 4 backward
def move_motor4_backward():
    GPIO.output(IN3_motor4, GPIO.LOW)
    GPIO.output(IN4_motor4, GPIO.HIGH)

# Function to stop Motor 4
def stop_motor4():
    GPIO.output(IN3_motor4, GPIO.LOW)
    GPIO.output(IN4_motor4, GPIO.LOW)

# Function to move all motors forward
def move_all_forward():
    move_motor1_forward()
    move_motor2_forward()
    move_motor3_forward()
    move_motor4_forward()

# Function to move all motors backward
def move_all_backward():
    move_motor1_backward()
    move_motor2_backward()
    move_motor3_backward()
    move_motor4_backward()

# Function to stop all motors
def stop_all():
    stop_motor1()
    stop_motor2()
    stop_motor3()
    stop_motor4()

# Function to turn 90 degrees using only two motors
def turn_90_degrees():
    move_motor1_forward()
    move_motor2_forward()
    stop_motor3()
    stop_motor4()
    time.sleep(1)  # Adjust time for accurate 90-degree turn
    stop_all()

# Test code to control the motors sequentially
try:
    while True:
        # Move Motor 1 forward
        print("Moving Motor 1 forward.")
        move_motor1_forward()
        time.sleep(2)  # Move Motor 1 for 2 seconds

        # Stop Motor 1
        print("Stopping Motor 1.")
        stop_motor1()
        time.sleep(2)  # Pause for 2 seconds

        # Move Motor 2 forward
        print("Moving Motor 2 forward.")
        move_motor2_forward()
        time.sleep(2)  # Move Motor 2 for 2 seconds

        # Stop Motor 2
        print("Stopping Motor 2.")
        stop_motor2()
        time.sleep(2)  # Pause for 2 seconds

        # Move all motors forward
        print("Moving all motors forward.")
        move_all_forward()
        time.sleep(2)  # Move all motors for 2 seconds

        # Stop all motors
        print("Stopping all motors.")
        stop_all()
        time.sleep(2)  # Pause for 2 seconds

        # Turn 90 degrees
        print("Turning 90 degrees.")
        turn_90_degrees()
        time.sleep(2)  # Pause for 2 seconds after turn

except KeyboardInterrupt:
    print("Program interrupted by the user.")
finally:
    stop_all()  # Ensure all motors are stopped
    GPIO.cleanup()  # Clean up GPIO settings
    print("GPIO cleaned up and program terminated.")
