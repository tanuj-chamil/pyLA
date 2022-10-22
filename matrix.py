from ast import Raise
from unittest import result
from xml.dom.minidom import Element


class Matrix:

    def __init__(self,elements) -> None:
        """
        Constructs all the necessary attributes for the Matrix object.

        Parameters
        ----------
            elements : list
        """
        if type(elements)!= list or type(elements[0])!=list:
            raise TypeError("Matrix must be a 2D-list")
        
        dimN = len(elements)
        dimM = len(elements[0])
        for row in elements[1:]:
            if len(row) != dimM:
                raise ValueError("Inconsistent row dimensions")

        self.dimN = dimN
        self.dimM = dimM
        self.elements = elements
    
    def dim(self):
        '''
        Returns the dimension of the matrix
                Parameters:
                    None
                Returns:
                    tuple (int): The dimension of the matrix
        '''
        return self.dimN, self.dimM


    def __str__(self) -> str:
        '''
        Returns the string representation of the matrix
                Parameters:
                    None
                Returns:
                    string (str): The string representation of the matrix 
        '''
        
        out = []
        for row in self.elements:
            out.append("\t".join(map(str,row)))
        string = "\n".join(out)
        return string

    def __add__(self,other):
        '''
        Returns sum of the matrix two matrices
                Parameters:
                    other (Matrix): A Matrix Object
                Returns:
                    result (Matrix): sum of the matrix two matrices
        '''
        if self.dim() != other.dim():
            raise IndexError("Dimensions do not match")

        result = []
        for n in range(self.dimN):
            result.append([self.elements[n][i]+ other.elements[n][i] for i in range(self.dimM)])
        
        return Matrix(result)