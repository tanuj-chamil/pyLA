class Matrix:

    def __init__(self,elements) -> None:
        """
        Constructs all the necessary attributes for the Matrix object.

        Parameters
        ----------
            elements : list
        """
        if type(elements)!= list or type(elements[0])!=list:
            raise TypeError("matrix must be a 2D-list")
        
        dimN = len(elements)
        dimM = len(elements[0])
        for row in elements[1:]:
            if len(row) != dimM:
                raise ValueError("inconsistent row dimensions")
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
        credits : georg from https://stackoverflow.com/a/13214945
        '''
        s = [[str(e) for e in row] for row in self.elements]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        out = [fmt.format(*row) for row in s]
        return 'Matrix=\n'+'\n'.join(out)

    def __add__(self,other):
        '''
        Returns sum of the matrix two matrices

        Parameters:
            other (Matrix): A matrix object
        Returns:
            result (Matrix): Sum of the matrix two matrices
        '''
        if self.dim() != other.dim():
            raise TypeError("dimensions do not match")

        result = []
        for n in range(self.dimN):
            result.append([self.elements[n][i]+ other.elements[n][i] for i in range(self.dimM)])
        
        return Matrix(result)

    def __sub__(self,other):
        '''
        Returns subtraction of the matrix two matrices

        Parameters:
            other (Matrix): A matrix object
        Returns:
            result (Matrix): Subtraction of the matrix two matrices
        '''
        if self.dim() != other.dim():
            raise TypeError("dimensions do not match")

        result = []
        for n in range(self.dimN):
            result.append([self.elements[n][i]- other.elements[n][i] for i in range(self.dimM)])
        
        return Matrix(result)


    def __mul__(self,other):
        '''
        Returns matrix-scalar multiplication or matrix-matrix multiplication
        
        Parameters:
            other (Matrix or int/float): A matrix object or scalar
        Returns:
            result (Matrix): matrix-scalar multiplication or matrix-matrix multiplication
        '''
        if type(other) == int or type(other)== float:
            result = []
            for n in range(self.dimN):
                result.append([self.elements[n][i]*other for i in range(self.dimM)])
            return Matrix(result)


    def __rmul__(self,other):
        '''
        Commutates scalar-matrix multiplication
        '''
        return self.__mul__(other)

    def getElement(self,row,column):
        return self.elements[row-1][column-1]

    def getRow(self,row):
        return self.elements[row-1]

    def rowOp(self,scale1,first,scale2,second,target):
        '''
        Returns row operated matrix where,
        target = scale1*first + scale2*second 
                Parameters:
                    target (int) : target row
                    scale1 (int) : scale of first row
                    first (int) : first row
                    scale2 (int) : scale of second row
                    second (int) : second row
                Returns:
                    result (Matrix):  Returns row operated matrix
        '''
        r1 = self.elements[first-1] 
        r2 = self.elements[second-1]
        self.elements[target-1] = [scale1*r1[i] + scale2*r2[i] for i in range(self.dimM)]

        return self

    def rowSwap(self,first,second):
        '''
        Returns row swapped matrix where,
        first <=> second 
                Parameters:
                    first (int) : first row
                    second (int) : second row
                Returns:
                    result (Matrix):  Returns row swapped matrix
        '''
        self.elements[first-1],self.elements[second-1] = self.elements[second-1],self.elements[first-1]
        return self

    def rowScale(self,row,scale):
        '''
        Returns row scaled matrix where,
        row = scale*row
                Parameters:
                    row (int) : row
                    scale (int) : scalar multiplier of row
                Returns:
                    result (Matrix):  Returns row swapped matrix
        '''
        self.elements[row-1] = [ scale*i for i in self.elements[row-1]]
        return self