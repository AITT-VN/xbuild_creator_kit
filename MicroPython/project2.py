from lcd_1602 import LCD1602
import dht

dht11 = dht.DHT11(Pin(pin21.pin))
lcd1602 = LCD1602(0)

last_check_time = 0

while True:
  # lấy thời gian hiện tại
  now = ticks_ms()
  if (now - last_check_time) >= 5000:
    # đã quá 5s kể từ lần cập nhật nhiệt độ cuối
    # cần cập nhật lại
    last_check_time = now
    dht11.measure()
    t = dht11.temperature()
    h = dht11.humidity()
    
    lcd1602.move_to(0, 0)
    lcd1602.putstr('Nhiet do: ' + str(t))
    lcd1602.move_to(0, 1)
    lcd1602.putstr('Do am: ' + str(h))
    
    if t < 32:
      pin31.write_digital(0)
      print('Tắt quạt')
    else:
      pin31.write_digital(1)
      print('Bật quạt')
