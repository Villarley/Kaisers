import Jetson.GPIO as GPIO
import time

# GPIO pin assignment for Motor 3
IN1_motor3 = 17  # GPIO17 -> Pin 11 on Jetson (Updated for BCM 17)
IN2_motor3 = 18  # GPIO18 -> Pin 12 on Jetson (Updated for BCM 18)

# GPIO pin assignment for Motor 4 (using new GPIO ports)
IN1_motor4 = 12  # GPIO12 -> Pin 32 on Jetson
IN2_motor4 = 6   # GPIO6 -> Pin 31 on Jetson

# GPIO setup
GPIO.setmode(GPIO.BCM)  # Use BCM numbering for GPIO pins
GPIO.setup(IN1_motor3, GPIO.OUT)
GPIO.setup(IN2_motor3, GPIO.OUT)
GPIO.setup(IN1_motor4, GPIO.OUT)
GPIO.setup(IN2_motor4, GPIO.OUT)

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

# Function to move Motor 4 forward (if needed)
def move_motor4_forward():
    print("Moving Motor 4 forward.")
    GPIO.output(IN1_motor4, GPIO.HIGH)
    GPIO.output(IN2_motor4, GPIO.LOW)

# Function to stop Motor 4 (if needed)
def stop_motor4():
    print("Stopping Motor 4.")
    GPIO.output(IN1_motor4, GPIO.LOW)
    GPIO.output(IN2_motor4, GPIO.LOW)

# Test code to control Motor 3 and setup Motor 4
try:
    # Move Motor 3 forward
    move_motor3_forward()
    time.sleep(2)  # Move Motor 3 for 2 seconds
    stop_motor3()
    time.sleep(1)  # Pause for 1 second

    # Optional: Move Motor 4 forward
    # move_motor4_forward()
    # time.sleep(2)  # Move Motor 4 for 2 seconds
    # stop_motor4()
    # time.sleep(1)  # Pause for 1 second

except KeyboardInterrupt:
    print("Program interrupted by the user.")
    stop_motor3()
    stop_motor4()
finally:
    stop_motor3()  # Ensure Motor 3 is stopped
    stop_motor4()  # Ensure Motor 4 is stopped
    GPIO.cleanup()  # Clean up GPIO settings
    print("GPIO cleaned up and program terminated.")
