import time

while True:
  sensor_value = pin41.read_analog()
  pin11.write_digital(1)
  time.sleep_ms(sensor_value)
  pin11.write_digital(0)
  time.sleep_ms(sensor_value)


