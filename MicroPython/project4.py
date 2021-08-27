import time

alarm_mode = False
pir_value = 0

while True:
  if btn_onboard.is_pressed():
    alarm_mode = not alarm_mode
    if alarm_mode:
      print('Chế độ bảo vệ được bật')
    else:
      print('Chế độ bảo vệ được tắt')
  
  pir_value = pin51.read_digital()
  if alarm_mode and pir_value == 1:
    print('Phát hiện có người xâm nhập')
    for count in range(5):
      led_onboard.show(0, (100, 0, 0))
      speaker.play(['F5:2'], wait=True)
      time.sleep(0.2)
      led_onboard.show(0, (0, 0, 0))
      speaker.play(['C5:2'], wait=True)
      time.sleep(0.2)
