# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 14:58:39 2022

@author: LiCheng_Xu
"""

import glob,platform

if platform.system() == 'Windows':
    split_char = '\\'
elif platform.system() == 'Linux':
    split_char = '/'
    
def gjf2xyz(gjf_dir,xyz_dir):
    gjf_files = glob.glob(gjf_dir+'*.gjf')
    
    for file in gjf_files:
        fn = file.split(split_char)[-1].split('.')[0]
        with open(file,'r') as fr:
            lines = fr.readlines()
        title = ''
        coord_start_idx = 0
        coord_end_idx = 0
        blank_line_num = 0
        blank_line_idx = []
        for idx,line in enumerate(lines):
            if line == '\n':
                blank_line_num += 1
                blank_line_idx.append(idx)
                
        title = lines[blank_line_idx[0]+1]
        coord_start_idx = blank_line_idx[1] + 2
        coord_end_idx = blank_line_idx[2]
        coord_lines = lines[coord_start_idx:coord_end_idx]
        
        xyz_string = '%d\n%s%s'%(len(coord_lines),title,''.join(coord_lines))
        
        with open(xyz_dir+fn+'.xyz','w') as fw:
            fw.writelines(xyz_string)
