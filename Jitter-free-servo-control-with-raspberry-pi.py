import RPi.GPIO as GPIO
import pigpio
import time 
servo = 13 #কোন পিন এ কানেক্ট করেছি সেটা বলে দিলাম। 
pwm = pigpio.pi() 
pwm.set_mode(servo, pigpio.OUTPUT)
pwm.set_PWM_frequency(servo, 50) #PWM ফ্রিকুএন্সি সেট করে দিলাম এটা ৫০ রাখলেই ভাল। 
print("0 deg")
pwm.set_servo_pulsewidth(servo, 500) ;
time.sleep(3)
print( "90 deg" )
pwm.set_servo_pulsewidth(servo, 1500) ;
time.sleep(3)
print("180 deg")
pwm.set_servo_pulsewidth(servo, 2500) ;
time.sleep(3)
print("0 deg")
pwm.set_servo_pulsewidth(servo, 500) ;
time.sleep(3)
pwm.set_PWM_dutycycle(servo, 0)
pwm.set_PWM_frequency(servo, 0)
