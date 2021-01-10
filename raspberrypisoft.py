import RPi.GPIO as GPIO
import time
import requests

URL = "http://nicolasryjou.pythonanywhere.com/api"

BASE_SERVO_PIN = 19
ARM_ONE_SERVO_PIN = 21
ARM_TWO_SERVO_PIN = 23
THREE_SERVO_PIN = 27

GPIO.setmode(GPIO.BOARD)

GPIO.setup(BASE_SERVO_PIN,GPIO.OUT)
base_servo = GPIO.PWM(THREE_SERVO_PIN,50)

GPIO.setup(ARM_ONE_SERVO_PIN,GPIO.OUT)
arm_1_servo = GPIO.PWM(THREE_SERVO_PIN,50)

GPIO.setup(ARM_TWO_SERVO_PIN,GPIO.OUT)
arm_2_servo = GPIO.PWM(THREE_SERVO_PIN,50)

GPIO.setup(THREE_SERVO_PIN,GPIO.OUT)
arm_3_servo = GPIO.PWM(THREE_SERVO_PIN,50)

# Start PWM running on both servos, value of 0 (pulse off)
base_servo.start(0)
arm_1_servo.start(0)
arm_2_servo.start(0)
arm_3_servo.start(0)

#Servo Pins

global angleServoOne
global angleServoTwo
global angleServoThree
global angleServoPull

angleServoOne = 0
angleServoTwo = 0
angleServoThree = 0
angleServoPull = False

def convert_to_action(input: str):
    if (input == "a"):
        angleServoThree += 3
    if (input == "b"):
        angleServoTwo += 3
    if (input == "c"):
        angleServoPull = False
    if (input == "d"):
        angleServoPull = True
    if (input == "e"):
        angleServoTwo -= 3
    if (input == "f"):
        angleServoThree -= 3
    if (input == "g"):
        angleServoOne -=3
    if (input == "h"):
        angleServoOne +=3
    else:
        print("_")

def servo_write(angle: int, pin: int):
    duty = angle / 18 + 2
    if pin == 1:
        GPIO.output(BASE_SERVO_PIN, True)
        base_servo.ChangeDutyCycle(duty)
        time.sleep(1)
        GPIO.output(BASE_SERVO_PIN, False)
        base_servo.ChangeDutyCycle(0)
    if pin == 2:
        GPIO.output(ARM_ONE_SERVO_PIN, True)
        arm_1_servo.ChangeDutyCycle(duty)
        time.sleep(1)
        GPIO.output(ARM_ONE_SERVO_PIN, False)
        arm_1_servo.ChangeDutyCycle(0)
    if pin == 3:
        GPIO.output(ARM_TWO_SERVO_PIN, True)
        arm_2_servo.ChangeDutyCycle(duty)
        time.sleep(1)
        GPIO.output(ARM_TWO_SERVO_PIN, False)
        arm_2_servo.ChangeDutyCycle(0)
    if pin == 4:
        GPIO.output(THREE_SERVO_PIN, True)
        arm_3_servo.ChangeDutyCycle(duty)
        time.sleep(1)
        GPIO.output(THREE_SERVO_PIN, False)
        arm_3_servo.ChangeDutyCycle(0)

class Move:

    def __init__(self):
        self.max_angle = 180

        self.base_servo = BASE_SERVO_PIN
        self.arm_one_servo = ARM_ONE_SERVO_PIN
        self.arm_two_servo = ARM_TWO_SERVO_PIN
        self.arm_three_servo = THREE_SERVO_PIN

    def rotate(self, angle: int):
        if angle < self.max_angle:
            servo_write(angle, self.base_servo)
        else:
            print("Angle limit reached. Limit : {} angles. Imposed angle: {}."
                  .format(self.max_angle, angle))


    def move_arm(self, arm: int = 1, angle: int = 90):
        if angle < self.max_angle:
            if arm == 1:
                servo_write(angle, self.arm_one_servo)

            if arm == 2:
                servo_write(angle, self.arm_two_servo)

    def actionDigger(self, status: bool):
        if status:
            servo_write(90, self.arm_three_servo)
        elif not status:
            servo_write(0, self.arm_three_servo)


robotic_arm = Move()

while True:
    r = requests.get(url=URL)
    data = r.json()
    convert_to_action(data[0])

    print(data)

    robotic_arm.rotate(angleServoOne)

    robotic_arm.move_arm(1, angleServoTwo)
    robotic_arm.move_arm(2, angleServoThree)

    robotic_arm.actionDigger(angleServoPull)

    time.sleep(0.1)
    if data[0] == "QUIT":
        base_servo.stop()
        arm_1_servo.stop()
        arm_2_servo.stop()
        arm_3_servo.stop()
        GPIO.cleanup()