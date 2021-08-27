import time

while True:
  print('AccelX: ', motion.get_accel('x'))
  print('AccelY: ', motion.get_accel('y'))
  print('AccelY: ', motion.get_accel('z'))
  
  print('GyroX:', motion.get_gyro_roll())
  print('GyroY:', motion.get_gyro_pitch())
  print('GyroZ:', motion.get_gyro_yaw())
  
  time.sleep_ms(100)


