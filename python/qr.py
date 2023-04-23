import os
import qrcode

img = qrcode.make("https://youtu.be/xvFZjo5Pg0")

img.save("qr.png", "PNG")

os.system("open qr.png")
