import time
from ir_receiver import *

ir_rx.start()

light_level = 0

while True:
  if ir_rx.get_code() == IR_REMOTE_UP:
    light_level = light_level + 50
    if light_level > 255:
      light_level = 255
    ir_rx.clear_code()
  elif ir_rx.get_code() == IR_REMOTE_DOWN:
    light_level = light_level - 50
    if light_level < 0:
      light_level = 0
    ir_rx.clear_code()
  elif ir_rx.get_code() == IR_REMOTE_SETUP:
    if light_level > 0:
      light_level = 0
    else:
      light_level = 255
    ir_rx.clear_code()
  led_onboard.show(0, (light_level, 0, 0))
  time.sleep(0.2)
