import time

while True:
  light_value = pin41.read_analog()
  print(light_value) # In giá trị cảm biến ánh sáng
  led_value = translate(light_value, 0, 4095, 0, 255)
  print(led_value) # In giá trị độ sáng của đèn đã được tính toán
  led_onboard.show(0, (led_value, 0, 0))
  time.sleep_ms(100)

