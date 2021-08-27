from ir_receiver import *
from lcd_1602 import LCD1602

lcd1602 = LCD1602(0)
lcd1602.backlight_on()

pass_code = '1234' # khai báo mật khẩu cố định
servo.position(0, 0)
ir_rx.start()

while True:
  if ir_rx.get_code() == IR_REMOTE_A:
    servo.position(0, 0) # khóa cửa lại
  elif ir_rx.get_code() == IR_REMOTE_B:
    # bắt đầu nhập mật mã
    lcd1602.clear()
    lcd1602.move_to(0, 0)
    lcd1602.putstr('Hay nhap mat ma:')
    input_code = ''
    while not (ir_rx.get_code() == IR_REMOTE_C):
      # liên tục đọc tín hiệu remote để nhập
      # mật mã cho đến khi phím C được nhấn
      print(ir_rx.get_raw_code())
      if ir_rx.get_code() == IR_REMOTE_0:
        input_code = input_code + '0'
        ir_rx.clear_code()
      if ir_rx.get_code() == IR_REMOTE_1:
        input_code = input_code + '1'
        ir_rx.clear_code()
      if ir_rx.get_code() == IR_REMOTE_2:
        input_code = input_code + '2'
        ir_rx.clear_code()
      if ir_rx.get_code() == IR_REMOTE_3:
        input_code = input_code + '3'
        ir_rx.clear_code()
      if ir_rx.get_code() == IR_REMOTE_4:
        input_code = input_code + '4'
        ir_rx.clear_code()
      if ir_rx.get_code() == IR_REMOTE_5:
        input_code = input_code + '5'
        ir_rx.clear_code()
      if ir_rx.get_code() == IR_REMOTE_6:
        input_code = input_code + '6'
        ir_rx.clear_code()
      if ir_rx.get_code() == IR_REMOTE_7:
        input_code = input_code + '7'
        ir_rx.clear_code()
      if ir_rx.get_code() == IR_REMOTE_8:
        input_code = input_code + '8'
        ir_rx.clear_code()
      if ir_rx.get_code() == IR_REMOTE_9:
        input_code = input_code + '9'
        ir_rx.clear_code()
      lcd1602.move_to(0, 1)
      lcd1602.putstr(input_code)
      time.sleep(0.5)
    # nhập mật mã đã xong, cần kiểm tra và hiện kết quả
    lcd1602.clear()
    if input_code == pass_code:
      lcd1602.move_to(0, 1)
      lcd1602.putstr('Mat ma dung')
      servo.position(0, 90)
    else:
      lcd1602.move_to(0, 1)
      lcd1602.putstr('Mat ma sai')
