from distutils.core import setup, Extension

module1 = Extension('mandelbrot', sources = ['mandelbrotmodule.c'])

setup (name = 'mandelbrot', version = '1.0', description = 'Mandelbrot generator', ext_modules = [module1])
