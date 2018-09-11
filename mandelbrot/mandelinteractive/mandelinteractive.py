import sys
import pygame
import numpy
import mandelbrot

def draw_mandel(window):
    pxarray = pygame.PixelArray(window)
    x_center = -1.0
    y_center =  0.0
    x_size = 100
    y_size = 100
    
    for xpos in xrange(x_size):
        a= mandelbrot.meta(x_size,y_size, xpos)
        for ypos in xrange(y_size): 
            pxarray[xpos][ypos] = (a[ypos], a[ypos], a[ypos])
        print xpos
        pygame.display.flip() 

pygame.init() 

#create the screen
window = pygame.display.set_mode((100,100)) 
draw_mandel(window)

pygame.display.flip() 

#input handling (somewhat boilerplate code):
while True: 
   for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
          sys.exit(0) 
      else: 
          print event 
