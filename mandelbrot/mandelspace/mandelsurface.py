from PIL import Image
import sys

def drawMandel(im, float_coord, pixel_coord, subpic_size):
    max_iteration = 1000
    x_center = -1.0
    y_center =  0.0
    print float_coord, pixel_coord, subpic_size
    for i in xrange(subpic_size[0]):
        for j in xrange(subpic_size[1]):
            x,y = ( x_center + 4.0*float(i - subpic_size[0]/2 )/subpic_size[0],
                      y_center + 4.0*float(j - subpic_size[1]/2)/subpic_size[1]
                    )

            a,b = float_coord
            iteration = 0

            while (a**2 + b**2 <= 4.0 and iteration < max_iteration):
                a,b = a**2 - b**2 + x, 2*a*b + y
                iteration += 1
            if iteration == max_iteration:
                color_value = 255 
            else:
                color_value = iteration*10 % 255
            im.putpixel( (pixel_coord[0]+i,pixel_coord[1]+j), (color_value, color_value, color_value))


im = Image.new("RGB", (10000,10000))

for row in xrange(1000):
    for column in xrange(1000):
        float_coord = (-5.0+float(column)/100.0, -5.0+float(row)/100.0)
        pixel_coord = (column*10, row*10)
        subpic_size = (10,10)
        drawMandel(im, float_coord, pixel_coord, subpic_size)


im.save("mandelbrot.png", "PNG")
