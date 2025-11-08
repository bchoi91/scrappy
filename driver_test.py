from gpiozero import Motor, PWMOutputDevice
from time import sleep

# LEFT SIDE (two motors together on left driver)
left_dir1 = 5
left_dir2 = 6
left_pwm_pin = 13

left_motor = Motor(forward=left_dir1, backward=left_dir2, pwm=False)
left_pwm = PWMOutputDevice(left_pwm_pin, frequency=20000)  # quiet motor PWM

# RIGHT SIDE (two motors together on right driver)
right_dir1 = 23
right_dir2 = 24
right_pwm_pin = 18

right_motor = Motor(forward=right_dir1, backward=right_dir2, pwm=False)
right_pwm = PWMOutputDevice(right_pwm_pin, frequency=20000)

def forward(speed=0.8):
    left_motor.forward()
    right_motor.forward()
    left_pwm.value = speed
    right_pwm.value = speed

def backward(speed=0.8):
    left_motor.backward()
    right_motor.backward()
    left_pwm.value = speed
    right_pwm.value = speed

def turn_left(speed=0.8):
    left_motor.backward()
    right_motor.forward()
    left_pwm.value = speed
    right_pwm.value = speed

def turn_right(speed=0.8):
    left_motor.forward()
    right_motor.backward()
    left_pwm.value = speed
    right_pwm.value = speed

def stop():
    left_motor.stop()
    right_motor.stop()
    left_pwm.value = 0
    right_pwm.value = 0

# -------------------
# TEST SEQUENCE
# -------------------
print("Forward...")
forward(0.7)
sleep(2)

print("Stop...")
stop()
sleep(1)

print("Backward...")
backward(0.7)
sleep(2)

print("Stop...")
stop()
sleep(1)

print("Turn Left...")
turn_left(0.7)
sleep(1.5)

print("Turn Right...")
turn_right(0.7)
sleep(1.5)

print("Stop")
stop()
