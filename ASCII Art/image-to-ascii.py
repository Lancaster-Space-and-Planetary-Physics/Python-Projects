#Made following https://gist.github.com/cdiener/10491632
#Import standard python modules
import os, sys

#Import third-party modules
import numpy as np
from PIL import Image

#Select input image
image_filepath = 'C:\\Users\\wiggsj\\Documents\\Practice Codes\\Python-Projects\\ASCII Art\\Input_images\\J_Wiggs_general_photo.jpg'

#Select ascii characters for use
ascii_chars = np.asarray(list(' .,:;irsXA253hMHGS#9B&@'))

#Set scaling factors
SC, GCF, WCF = .1, 1, 7/4

#Open image
im = Image.open(image_filepath)

#Do the smart stuff
S = (round(im.size[0]*SC*WCF), round(im.size[1]*SC))
im = np.sum(np.asarray(im.resize(S)), axis=2)
im -= im.min()
im = (1.0 - im/im.max())**GCF*(ascii_chars.size-1)

print( "\n".join( ("".join(r) for r in ascii_chars[im.astype(int)]) ) )
