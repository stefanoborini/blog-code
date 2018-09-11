from PIL import Image

im = Image.new("RGB", (300,300))
for i in xrange(300):
    print "i = ",i
    for j in xrange(300):
        x0 = float( 4.0*float(i-150)/300.0 -1.0)
        y0 = float( 4.0*float(j-150)/300.0 +0.0)
        x=0.0
        y=0.0
        iteration = 0
        max_iteration = 1000
        while (x*x + y*y <= 4.0 and iteration < max_iteration):
            xtemp = x*x - y*y + x0
            y = 2.0*x*y+y0
            x = xtemp
            iteration += 1
        if iteration == max_iteration:
            value = 255 
        else:
            value = iteration*10 % 255
        print value 
        im.putpixel( (i,j), (value, value, value))

im.save("image.png", "PNG")
