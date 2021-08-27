import time

light_sensor = 0 # giá trị của cảm biến ánh sáng
pir_value = 0 # trạng thái của cảm biến chuyển động PIR
led_value = 0 # trạng thái bật tắt hiện tại của đèn LED
led_on_time = 0 # thời gian lúc đèn được bật lên

while True:
  light_sensor = pin41.read_analog()
  pir_value = pin51.read_digital()
  
  if pir_value == 1 and light_sensor < 200:
    pin61.write_digital(1)
    led_on_time = time.ticks_ms()
    led_value = 1
  
  now = time.ticks_ms()
  if led_value == 1 and now - led_on_time >= 10000:
    pin61.write_digital(0)
    led_on_time = 0
    led_value = 0
