import sys

from PIL import Image

im = Image.open(sys.argv[1])
white = 0
black = 0
for i in im.getdata():
    if i == (255,255,255):
        white += 1
    else:
        # we assume black everything that is not white:
        black += 1
print im.size[0],im.size[1],white,black
