import time

# Phát bài nhạc Twinkle twinkle little stars
# Câu 1: Đồ, Đồ, Son, Son, La, La, Son
def song_1():
  speaker.play(['C4:1'], wait=True)
  speaker.play(['C4:1'], wait=True)
  speaker.play(['G4:1'], wait=True)
  speaker.play(['G4:1'], wait=True)
  speaker.play(['A4:1'], wait=True)
  speaker.play(['A4:1'], wait=True)
  speaker.play(['G4:1'], wait=True)

# Câu 2: Fa, Fa, Mi, Mi, Rê, Rê, Đồ
def song_2():
  speaker.play(['F4:1'], wait=True)
  speaker.play(['F4:1'], wait=True)
  speaker.play(['E4:1'], wait=True)
  speaker.play(['E4:1'], wait=True)
  speaker.play(['D4:1'], wait=True)
  speaker.play(['D4:1'], wait=True)
  speaker.play(['C4:1'], wait=True)


while True:
  song_1()
  time.sleep(0.5)
  song_2()
  time.sleep(1)
