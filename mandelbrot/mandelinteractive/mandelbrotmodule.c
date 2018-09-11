#include "Python.h"
#include "math.h"

static int 
quick_mandel(double a_init, double b_init)
{
    double a, a_tmp, b;
    double x_center, y_center;
    long x_size, y_size;
    double x,y;
    long iteration, color;
    PyObject *list;
    long i,j;
    int err;
    
    x_size = 60;
    y_size = 60;
    x_center = -1.0;
    y_center = 0.0;

    for (i = 0; i < x_size; i++) 
    {
       for (j = 0; j < y_size; j++) 
       {
            x = x_center + 4.0 * (double)(i - x_size/2) / (double)x_size;
            y = y_center + 4.0 * (double)(j - y_size/2) / (double)y_size;
            iteration = 0;
            a = a_init; b = b_init;

            while (pow(a,2) + pow(b,2) <= 4.0 && iteration < 1000) 
            {
                a_tmp = a;
                a = pow(a,2) - pow(b,2) + x;
                b = 2*a_tmp*b + y;
                iteration++;
            }
            if (iteration == 1000) { return 1; } 
       }
    }

    return 0;
}

static PyObject *
mandelbrot_generate(PyObject *self, PyObject *args)
{
    double a, a_tmp, b, a_init, b_init;
    double x_center, y_center;
    long x_size, y_size;
    double x,y;
    long iteration, color;
    PyObject *list;
    long i,j;
    int err;

    if (!PyArg_ParseTuple(args, "ddddll", &a_init, &b_init, &x_center, &y_center, &x_size, &y_size)) return NULL;
    list = PyList_New(x_size*y_size);
    Py_INCREF(list);

    for (i = 0; i < x_size; i++) 
    {
       for (j = 0; j < y_size; j++) 
       {
            x = x_center + 4.0 * (double)(i - x_size/2) / (double)x_size;
            y = y_center + 4.0 * (double)(j - y_size/2) / (double)y_size;
            iteration = 0;
            a = a_init; b = b_init;

            while (pow(a,2) + pow(b,2) <= 4.0 && iteration < 1000) 
            {
                a_tmp = a;
                a = pow(a,2) - pow(b,2) + x;
                b = 2*a_tmp*b + y;
                iteration++;
            }
            if (iteration == 1000) 
            {
                color = 255;
            } 
            else
            {
                color = (long)( iteration * 10 % 255 );
            }
            err = PyList_SetItem(list, (i*y_size)+j, PyInt_FromLong(color));
       }
    }


    return list;
}

static PyObject *
mandelbrot_meta(PyObject *self, PyObject *args)
{
    long x_size, y_size;
    double x,y;
    long color;
    PyObject *list;
    long i,j, xpos;

    if (!PyArg_ParseTuple(args, "lll", &x_size, &y_size, &xpos)) return NULL;
    list = PyList_New(y_size);
    Py_INCREF(list);

    for (i = 0; i < y_size; i++) 
    {
        //x = -3.0+(double)(xpos+1)/(double)(x_size*6.0); 
        //y = -1.5+(double)(i+1)/(double)(y_size*3.0);
        x = 0.0;
        y = 0.0;
        if (quick_mandel(x,y))
        {
            color = 255;
        } 
        else
        {
            color = 0;
        }
        PyList_SetItem(list, i, PyInt_FromLong(color));
    }

    return list;
}


PyMethodDef MandelbrotMethods[] = {
    {"generate", mandelbrot_generate, METH_VARARGS, "Generates mandelbrot data"},
    {"meta", mandelbrot_meta, METH_VARARGS, "Generates meta mandelbrot data"},
    {NULL, NULL, 0, NULL},
};


PyMODINIT_FUNC
initmandelbrot()
{
    (void)Py_InitModule("mandelbrot", MandelbrotMethods);
}


