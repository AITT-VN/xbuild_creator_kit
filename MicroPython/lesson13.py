import time

while True:
  sensor_value = pin41.read_analog()
  servo_value = translate(sensor_value, 0, 4095, 0, 180)
  servo.position(0, servo_value)
  time.sleep_ms(50)


