for y in range(40):
    for x in range(40):
        c=complex(x/17.0-2,y/17.0-1.5)
        z=c-c
        i=0
        while i<28 and abs(z)<2:
            z=z*z+c
            i+=1
        print ".-+oxawOX "[i/3],
    print

