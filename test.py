import Jetson.GPIO as GPIO
import time

class MotorControl:
    def __init__(self):
        # GPIO pin assignment for Motor 1
        self.IN1_motor1 = 19  # GPIO19 -> Pin 35 on Jetson
        self.IN2_motor1 = 26  # GPIO26 -> Pin 37 on Jetson

        # GPIO pin assignment for Motor 2
        self.IN3_motor2 = 20  # GPIO20 -> Pin 38 on Jetson
        self.IN4_motor2 = 16  # GPIO16 -> Pin 36 on Jetson

        # GPIO pin assignment for Motor 3
        self.IN1_motor3 = 17  # GPIO17 -> Pin 11 on Jetson
        self.IN2_motor3 = 18  # GPIO18 -> Pin 12 on Jetson

        # GPIO pin assignment for Motor 4
        self.IN3_motor4 = 12  # GPIO12 -> Pin 32 on Jetson
        self.IN4_motor4 = 6   # GPIO6 -> Pin 31 on Jetson

        # Setup GPIO
        GPIO.setmode(GPIO.BCM)  # Use BCM numbering for GPIO pins
        GPIO.setup(self.IN1_motor1, GPIO.OUT)
        GPIO.setup(self.IN2_motor1, GPIO.OUT)
        GPIO.setup(self.IN3_motor2, GPIO.OUT)
        GPIO.setup(self.IN4_motor2, GPIO.OUT)
        GPIO.setup(self.IN1_motor3, GPIO.OUT)
        GPIO.setup(self.IN2_motor3, GPIO.OUT)
        GPIO.setup(self.IN3_motor4, GPIO.OUT)
        GPIO.setup(self.IN4_motor4, GPIO.OUT)

    def move_motor_forward(self, motor_num):
        if motor_num == 1:
            print("Moving Motor 1 forward.")
            GPIO.output(self.IN1_motor1, GPIO.HIGH)
            GPIO.output(self.IN2_motor1, GPIO.LOW)
        elif motor_num == 2:
            print("Moving Motor 2 forward.")
            GPIO.output(self.IN3_motor2, GPIO.HIGH)
            GPIO.output(self.IN4_motor2, GPIO.LOW)
        elif motor_num == 3:
            print("Moving Motor 3 forward.")
            GPIO.output(self.IN1_motor3, GPIO.HIGH)
            GPIO.output(self.IN2_motor3, GPIO.LOW)
        elif motor_num == 4:
            print("Moving Motor 4 forward.")
            GPIO.output(self.IN3_motor4, GPIO.LOW)   # Corrected direction
            GPIO.output(self.IN4_motor4, GPIO.HIGH)  # Corrected direction
        else:
            print("Invalid motor number.")

    def move_motor_backward(self, motor_num):
        if motor_num == 1:
            print("Moving Motor 1 backward.")
            GPIO.output(self.IN1_motor1, GPIO.LOW)
            GPIO.output(self.IN2_motor1, GPIO.HIGH)
        elif motor_num == 2:
            print("Moving Motor 2 backward.")
            GPIO.output(self.IN3_motor2, GPIO.LOW)
            GPIO.output(self.IN4_motor2, GPIO.HIGH)
        elif motor_num == 3:
            print("Moving Motor 3 backward.")
            GPIO.output(self.IN1_motor3, GPIO.LOW)
            GPIO.output(self.IN2_motor3, GPIO.HIGH)
        elif motor_num == 4:
            print("Moving Motor 4 backward.")
            GPIO.output(self.IN3_motor4, GPIO.HIGH)
            GPIO.output(self.IN4_motor4, GPIO.LOW)
        else:
            print("Invalid motor number.")

    def stop_motor(self, motor_num):
        if motor_num == 1:
            print("Stopping Motor 1.")
            GPIO.output(self.IN1_motor1, GPIO.LOW)
            GPIO.output(self.IN2_motor1, GPIO.LOW)
        elif motor_num == 2:
            print("Stopping Motor 2.")
            GPIO.output(self.IN3_motor2, GPIO.LOW)
            GPIO.output(self.IN4_motor2, GPIO.LOW)
        elif motor_num == 3:
            print("Stopping Motor 3.")
            GPIO.output(self.IN1_motor3, GPIO.LOW)
            GPIO.output(self.IN2_motor3, GPIO.LOW)
        elif motor_num == 4:
            print("Stopping Motor 4.")
            GPIO.output(self.IN3_motor4, GPIO.LOW)
            GPIO.output(self.IN4_motor4, GPIO.LOW)
        else:
            print("Invalid motor number.")

    def move_all_forward(self):
        print("Moving all motors forward.")
        self.move_motor_forward(1)
        self.move_motor_forward(2)
        self.move_motor_forward(3)
        self.move_motor_forward(4)

    def move_all_backward(self):
        print("Moving all motors backward.")
        self.move_motor_backward(1)
        self.move_motor_backward(2)
        self.move_motor_backward(3)
        self.move_motor_backward(4)

    def stop_all(self):
        print("Stopping all motors.")
        self.stop_motor(1)
        self.stop_motor(2)
        self.stop_motor(3)
        self.stop_motor(4)

    def turn_left(self):
        print("Turning left.")
        self.move_motor_forward(1)
        self.move_motor_forward(3)
        self.move_motor_backward(2)
        self.move_motor_backward(4)

    def turn_right(self):
        print("Turning right.")
        self.move_motor_forward(2)
        self.move_motor_forward(4)
        self.move_motor_backward(1)
        self.move_motor_backward(3)

    def cleanup(self):
        print("Cleaning up GPIO settings.")
        GPIO.cleanup()

# Example usage
if __name__ == "__main__":
    motor_control = MotorControl()

    try:
        # Move all motors forward
        motor_control.move_all_forward()
        time.sleep(2)
        motor_control.stop_all()
        time.sleep(1)

        # Move all motors backward
        motor_control.move_all_backward()
        time.sleep(2)
        motor_control.stop_all()
        time.sleep(1)

        # Turn left
        motor_control.turn_left()
        time.sleep(2)
        motor_control.stop_all()
        time.sleep(1)

        # Turn right
        motor_control.turn_right()
        time.sleep(2)
        motor_control.stop_all()
        time.sleep(1)

    except KeyboardInterrupt:
        print("Program interrupted by the user.")
        motor_control.cleanup()
    finally:
        motor_control.cleanup()
        print("GPIO cleaned up and program terminated.")
