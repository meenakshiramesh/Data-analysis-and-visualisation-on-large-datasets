import numpy
import matplotlib.pyplot as plt

axes_value = numpy.arange(-100,100,10)
[dy, dx] = numpy.meshgrid(axes_value, axes_value)


function = 2*dx+3*dy

print(function)
plt.imshow(function)
plt.title("function of plot 2dx+3dy")
plt.savefig('myfig.png')