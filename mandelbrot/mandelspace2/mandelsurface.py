from PIL import Image
import numpy
import sys

image_size = (100,100)
mandel_size = (10,10)

def drawMandel(float_coord):
    global mandel_size
    
    average_color = 0.0
    max_iteration = 1000
    white = 0
    x_center = -1.0
    y_center =  0.0
    print float_coord
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
                color_value = 255 
                white += 1
            else:
                color_value = iteration*10 % 255

    return white

im = Image.new("RGB", image_size)

a=numpy.zeros( image_size, dtype=numpy.int)

for row in xrange(image_size[0]):
    for column in xrange(image_size[1]):
        float_coord = (-3.0+float(row)/float(image_size[0])*6.0, -3.0+float(column)/float(image_size[1])*6.0)
        white = drawMandel(float_coord)
        a[row][column] = white

b=255*a/a.max()
b.astype(int)
print b
for row in xrange(image_size[0]):
    for column in xrange(image_size[1]):
        if b[row][column]:
            im.putpixel( (row, column), (255,255,255))
        else:
            im.putpixel( (row, column), (0,0,0))
            
im.save("mandelbrot.png", "PNG")
