from ir_receiver import *

ir_rx.start()

while True:
  if ir_rx.get_code() == IR_REMOTE_A:
    led_onboard.show(0, (255, 0, 0))
    ir_rx.clear_code()
  elif ir_rx.get_code() == IR_REMOTE_B:
    led_onboard.show(0, (0, 255, 0))
    ir_rx.clear_code()
  elif ir_rx.get_code() == IR_REMOTE_C:
    led_onboard.show(0, (0, 0, 255))
    ir_rx.clear_code()
  elif ir_rx.get_code() == IR_REMOTE_D:
    led_onboard.show(0, (255, 255, 255))
    ir_rx.clear_code()
  else:
    led_onboard.show(0, (0, 0, 0))
    ir_rx.clear_code()
