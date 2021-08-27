import time
from lcd_1602 import LCD1602

lcd1602 = LCD1602(0)
lcd1602.backlight_on()

while True:
  lcd1602.move_to(0, 0)
  lcd1602.putstr('OhStem')
   
  lcd1602.move_to(0, 1)
  lcd1602.putstr('Xin chao ban')
  time.sleep(2)
   
  lcd1602.clear()
  time.sleep(1)
