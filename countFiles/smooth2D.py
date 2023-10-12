# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 17:15:29 2023

@author: lixianlong
"""


import numpy as np
from scipy.sparse import spdiags

def smooth2D(matrixIn, **kawrgs):
    '''
    Smooths 2D array data, and ignore NAN datas.
    matrixOut = smooth2D(matrixIn, Nr=, Nc=)
    Parameters
    ----------
    matrixIn : Original matrix
    **kawrgs : single
        there are 2 variables in kawrgs, "Nr" and "Nc". "Nr" is the number
        of points used to smooth rows, and "Nc" is number of points to 
        smooth columns. If not specified, "Nc" = "Nr".
    Returns
    -------
    matrixOut: smoothed version of original matrix

    '''
    if len(kawrgs)<1:
        print('Not enough input arguments')
    else:
        nr = kawrgs['Nr']
        if len(kawrgs)<2:
            nc = nr
        else:
            nc = kawrgs['Nc']
    
    row = matrixIn.shape[0]
    col = matrixIn.shape[1]
    
    aa = np.ones([row,2*nr+1]).T
    bb = np.arange(-nr,nr+1,1)
    eL = spdiags(aa,bb,row,row)
    aa = np.ones([col,2*nr+1]).T
    bb = np.arange(-nr,nr+1,1)
    eR = spdiags(aa,bb,col,col)
    
    A = np.empty([row,col])
    for i in range(0,row):
        for j in range(0,col):
            if np.isnan(matrixIn[i,j]):
                A[i,j]=0
            else:
                A[i,j]=1
    
    matrixIn[np.isnan(matrixIn)]=0
    nrmlize = eL*(A)*eR
    
    for i in range(0,row):
        for j in range(0,col):
            if A[i,j] == 0:
               nrmlize[i,j]=np.nan
    
    matrixOut = eL*matrixIn*eR;
    matrixOut = matrixOut/nrmlize;
    return matrixOut
        
            
    
    
    




