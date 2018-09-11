from PIL import Image
import sys

image_size = (30000,30000)
mandel_size = (10,10)

def drawMandel(float_coord):
    global mandel_size
    
    average_color = 0.0
    max_iteration = 1000
    x_center = -1.0
    y_center =  0.0
    for row in xrange(mandel_size[0]):
        for column in xrange(mandel_size[1]):
            x,y = ( x_center + 4.0*float(column - mandel_size[1]/2 )/mandel_size[1],
                      y_center + 4.0*float(row - mandel_size[0]/2)/mandel_size[0]
                    )

            a,b = float_coord
            iteration = 0

            while (a**2 + b**2 <= 4.0 and iteration < max_iteration):
                a,b = a**2 - b**2 + x, 2*a*b + y
                iteration += 1
            if iteration == max_iteration:
                return True
            else:
                continue

    return False

im = Image.new("RGB", image_size)

for row in xrange(image_size[0]):
    print row
    for column in xrange(image_size[1]):
        float_coord = (-3.0+float(row+1)/float(image_size[0])*6.0, -1.5+float(column+1)/float(image_size[1])*3.0)
        white = drawMandel(float_coord)
        if white:
            im.putpixel( (row, column), (255,255,255))
        else:
            im.putpixel( (row, column), (0,0,0))

im.save("mandelbrot.png", "PNG")
