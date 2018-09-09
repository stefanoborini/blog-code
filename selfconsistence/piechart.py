import sys
from matplotlib import pyplot

white = int(sys.argv[1])
black = int(sys.argv[2])

pyplot.pie([white, black], colors=('w', 'k'))
pyplot.savefig(sys.argv[3], format="pdf")
