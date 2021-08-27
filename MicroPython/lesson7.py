import time

led_state = 0

while True:
  sound_value = pin41.read_analog()
  
  if sound_value > 1000:
    led_state = 1 - led_state
    time.sleep(0.3)
  
  if led_state == 0:
    led_onboard.show(0, (0, 0, 0))
  else:
    led_onboard.show(0, (255, 0, 0))
  
  time.sleep(10)
