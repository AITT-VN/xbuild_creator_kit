import time
import dht
from lcd_1602 import LCD1602

lcd1602 = LCD1602(0)
dht_pin = Pin(pin21.pin)
dht11 = dht.DHT11(dht_pin)

while True:
  dht11.measure()
  lcd1602.clear()
  lcd1602.move_to(0, 0)
  lcd1602.putstr('Nhiet do: ' + str(dht11.temperature()))
  lcd1602.move_to(0, 1)
  lcd1602.putstr('Do am: ' + str(dht11.humidity()))
  time.sleep(5)
