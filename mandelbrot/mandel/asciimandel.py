
for i in xrange(40):
    line = []
    for j in xrange(80):
        x0 = float( 4.0*float(i-20)/40.0 -1.0)
        y0 = float( 4.0*float(j-40)/80.0 +0.0)
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
            line.append(" ")
        else:
            line.append("*")
    print "".join(line)

