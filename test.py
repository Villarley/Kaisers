import Jetson.GPIO as GPIO
import time

# GPIO pin assignment for Motor 3
IN1_motor3 = 17  # GPIO17 -> Pin 11 on Jetson (Updated for BCM 17)
IN2_motor3 = 18  # GPIO18 -> Pin 12 on Jetson (Updated for BCM 18)

# GPIO setup
GPIO.setmode(GPIO.BCM)  # Use BCM numbering for GPIO pins
GPIO.setup(IN1_motor3, GPIO.OUT)
GPIO.setup(IN2_motor3, GPIO.OUT)

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

# Test code to control Motor 3
try:
    # Move Motor 3 forward
    move_motor3_forward()
    time.sleep(2)  # Move Motor 3 for 2 seconds
    stop_motor3()
    time.sleep(1)  # Pause for 1 second

except KeyboardInterrupt:
    print("Program interrupted by the user.")
    stop_motor3()
finally:
    stop_motor3()  # Ensure Motor 3 is stopped
    GPIO.cleanup()  # Clean up GPIO settings
    print("GPIO cleaned up and program terminated.")
