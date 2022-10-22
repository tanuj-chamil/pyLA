class Matrix:

    def __init__(self,elements) -> None:
        """
        Constructs all the necessary attributes for the Matrix object.

        Parameters
        ----------
            elements : list
        """

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