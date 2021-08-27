while True:
  sensor_value = pin41.read_analog()
  pwm_value = translate(sensor_value, 0, 4095, 0, 1023)
  pin11.write_analog(pwm_value)
