import matplotlib.image as mpimg
import sys

img = mpimg.imread(sys.argv[1])
trim = img[:64,:64]

mpimg.imsave(sys.argv[1],trim)
