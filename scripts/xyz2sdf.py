# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 20:45:53 2020

@author: Li-Cheng Xu
"""


from openbabel.pybel import (readfile,Outputfile) 
def MolFormatConversion(input_file:str,output_file:str,input_format="xyz",output_format="sdf"):
    molecules = readfile(input_format,input_file)
    output_file_writer = Outputfile(output_format,output_file,overwrite=True)
    for i,molecule in enumerate(molecules):
        output_file_writer.write(molecule)
    output_file_writer.close()
    print('%d molecules converted'%(i+1))
