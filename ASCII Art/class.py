# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 13:24:07 2021

@author: ellio
"""

import numpy as np
import PIL
from PIL import ImageOps

class Ascii_Imager():
    
    def __init__(self, fname:str, ascii_chars=None, compress:int=2):
        
        """
        Loads in an Image file and converts it to ascii character art
        
        ----------
        Parameters
        ----------
        
        fname: str
            filename of image to convert to ascii
            
        ascii_chars: list (optional)
            list of ascii characters. If not provided will use default list
            instead (recommended)
            
        compress: int (optional)
            if 1, does nothing. If even number, will compress image resolution
            by to original resolution/compress using a mean filter
            
        -------
        Outputs
        -------
        
        Text file sharing same name as input fname of ascii character art
        
        """
        
        if ascii_chars == None:
            #ascii characters should decrease in intensity
            self.ascii_chars = ["@", "&", "%", "£", "$", "?", "!", ":", "*", 
                                "+", "-", ".", " "]
            
        #load image and convert to greyscale values
        self.image = PIL.Image.open(fname)     
        self.grey_image = ImageOps.grayscale(self.image)
        self.grey_vals = np.array(self.grey_image)
        
        #get range of greyscale numeric values
        min_num = np.amin(self.grey_vals)
        max_num = np.amax(self.grey_vals)
        step = (max_num - min_num)/(len(self.ascii_chars)-1)
        
        #get shape of image
        nrows = self.grey_vals.shape[0]
        ncolumns = self.grey_vals.shape[1]
        
        #compress image
        if compress > 1:
            if compress % 2 != 0:
                raise ValueError("compress must be divisible by 2")
            else:
                old_nrows = nrows
                nrows = int(nrows/compress)
                old_ncolumns = ncolumns
                ncolumns = int(ncolumns/compress)
                self.grey_vals = self.grey_vals.reshape(nrows, old_nrows//nrows, 
                                                        ncolumns, old_ncolumns//ncolumns,
                                                        ).mean(3).mean(1)
        
        #initialise ascii art string
        self.ascii = ""
        
        #for each row
        for y in range(nrows):
            #convert row from nums to list of ascii characters
            ascii_row = [self.ascii_chars[int(num//step)] for num in self.grey_vals[y]]
            #convert list to string and add to ascii
            self.ascii = self.ascii + "".join(ascii_row) + "\n"
    
        #save to file
        save_fname = fname[:-4]+".txt"
        with open(save_fname, "w") as f:
            f.write(self.ascii)
                
        return

    
if __name__ == "__main__":
    
    im = Ascii_Imager("hodor.jpg", compress=1)