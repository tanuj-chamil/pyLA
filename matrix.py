from ast import Raise


class Matrix:

    def __init__(self,elements) -> None:
        """
        Constructs all the necessary attributes for the Matrix object.

        Parameters
        ----------
            elements : list
        """
        if type(elements)!= list or type(elements[0])!=list:
            raise TypeError
        
        dimN = len(elements[0])
        for row in elements[1:]:
            if len(row) != dimN:
                raise ValueError

        self.elements = elements

    def __str__(self) -> str:
        '''
        Returns the string representation of the matrix
                Parameters:
                    self (Matrix): A Matrix Object
                Returns:
                    string (str): The string representation of the matrix 
        '''

        out = []
        for row in self.elements:
            out.append("\t".join(map(str,row)))
        string = "\n".join(out)
        return string