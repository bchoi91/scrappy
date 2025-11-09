from gpiozero import Motor, PWMOutputDevice
from time import sleep

# LEFT SIDE A
left_dir1a = 6
left_dir2a = 7
left_pwm_pina = 18

left_motora = Motor(forward=left_dir1a, backward=left_dir2a, pwm=False)
left_pwma = PWMOutputDevice(left_pwm_pina, frequency=2000)  # quiet motor PWM

# LEFT SIDE B
left_dir1b = 16
left_dir2b = 17
left_pwm_pinb = 19

left_motorb = Motor(forward=left_dir1b, backward=left_dir2b, pwm=False)
left_pwmb = PWMOutputDevice(left_pwm_pinb, frequency=2000)  # quiet motor PWM

# # RIGHT SIDE (two motors together on right driver)
# right_dir1a = 7
# right_dir2a = 1
# right_pwm_pina = 12
# right_motora = Motor(forward=right_dir1a, backward=right_dir2a, pwm=False)
# right_pwma = PWMOutputDevice(right_pwm_pina, frequency=2000)

# # RIGHT SIDE (two motors together on right driver)
# right_dir1b = 14
# right_dir2b = 15
# right_pwm_pinb = 18

# right_motorb = Motor(forward=right_dir1b, backward=right_dir2b, pwm=False)
# right_pwmb = PWMOutputDevice(right_pwm_pinb, frequency=2000)

def forward(speed=0.8):
    left_motora.forward()
    # right_motora.forward()
    # right_motora.forward()
    left_pwma.value = speed
    # right_pwma.value = speed

    left_motorb.forward()
    # right_motorb.forward()
    left_pwmb.value = speed
    # right_pwmb.value = speed

# def backward(speed=0.8):
#     left_motora.backward()
#     right_motor.backward()
#     left_pwma.value = speed
#     right_pwm.value = speed

# def turn_left(speed=0.8):
#     left_motora.backward()
#     right_motor.forward()
#     left_pwma.value = speed
#     right_pwm.value = speed

# def turn_right(speed=0.8):
#     left_motora.forward()
#     right_motor.backward()
#     left_pwma.value = speed
#     right_pwm.value = speed

# def stop():
#     left_motora.stop()
#     right_motor.stop()
#     left_pwma.value = 0
#     right_pwm.value = 0

# -------------------
# TEST SEQUENCE
# -------------------
print("Forward...")
forward(0.7)
sleep(2)

# print("Stop...")
# stop()
# sleep(1)

# print("Backward...")
# backward(0.7)
# sleep(2)

# print("Stop...")
# stop()
# sleep(1)

# print("Turn Left...")
# turn_left(0.7)
# sleep(1.5)

# print("Turn Right...")
# turn_right(0.7)
# sleep(1.5)

# print("Stop")
# stop()
