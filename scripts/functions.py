# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 19:20:54 2021

@author: Li-Cheng Xu
"""
import random,rdkit
import numpy as np

def RandSel(List):
    return List[random.randint(0,len(List)-1)]
def encode_hybrid_types(hybrid_tpye):
    hybrid_types = sorted(list(rdkit.Chem.rdchem.HybridizationType.names.keys()))
    hybrid_encodes = np.zeros(len(hybrid_types))
    hybrid_encodes[hybrid_types.index(hybrid_tpye)] += 1
    return hybrid_encodes
