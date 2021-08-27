while True:
  if (btn_onboard.is_pressed()):
    pin11.write_digital(1)
  else:
    pin11.write_digital(0)
