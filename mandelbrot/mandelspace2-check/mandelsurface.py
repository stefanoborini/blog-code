from PIL import Image
import numpy
import sys

image_size = (10,10)
mandel_size = (100,100)

def drawMandel(float_coord):
    global mandel_size
    
    im = Image.new("RGB", mandel_size)
    average_color = 0.0
    max_iteration = 1000
    white = 0
    x_center = -1.0
    y_center =  0.0
    print float_coord
    for row in xrange(mandel_size[0]):
        for column in xrange(mandel_size[1]):
            x,y = ( x_center - 2.0 + 4.0*float(column)/float(mandel_size[1]),
                      y_center + 2.0 - 4.0*float(row)/float(mandel_size[0])
                    )
            print x,y, row,column
            a,b = float_coord
            iteration = 0

            while (a**2 + b**2 <= 4.0 and iteration < max_iteration):
                a,b = a**2 - b**2 + x, 2*a*b + y
                iteration += 1
            if iteration == max_iteration:
                color_value = 255 
                white += 1
            else:
                color_value = iteration*10 % 255
            im.putpixel( (column, row), (color_value, color_value, color_value))
    
    im.save("mandelbrot-"+str(float_coord)+".png", "PNG")

    return white

float_coord = (0.0, 0.0)
white = drawMandel(float_coord)
