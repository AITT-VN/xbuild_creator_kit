import time

while True:
  pin11.write_digital(1)
  time.sleep(1)
  pin11.write_digital(0)
  time.sleep(1)
