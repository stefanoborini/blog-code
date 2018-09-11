from PIL import Image

x0 = 0.1
y0 = 0.1
x=0.0
y=0.0
iteration = 0
max_iteration = 1000
while (x*x + y*y <= 4.0 and iteration < max_iteration):
    xtemp = x*x - y*y + x0
    y = 2.0*x*y+y0
    x = xtemp
    print x,y
    iteration += 1
