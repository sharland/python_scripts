#from __future__ import print_function       # for python2 compat

import sys; from PIL import Image; import numpy as np

#chars = np.asarray(list(' .,:;irsXA253hMHGS#9B&@'))

chars = np.asarray(list(' .,:;irsXA253hMHGS#9B&@'))



f = "building2.JPG"
SC= .14
GCF= 1.8
WCF= 7/4
img = Image.open(f)
S = ( round(img.size[0]*SC*WCF),  round(img.size[1]*SC) )
img = np.sum( np.asarray( img.resize(S) ), axis=2)
img -= img.min()
img = (1.0 - img/img.max())**GCF*(chars.size-1)

print( "\n".join( ("".join(r) for r in   chars[img.astype(int)]) ) )
