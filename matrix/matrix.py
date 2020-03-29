import numpy
from latex.latex_convertable import LatexConvertable

class Matrix(LatexConvertable):

    """ numpy.array wrapper for common operations """

    def __init__(self, matrix):
        self.array = numpy.array(matrix)

    @property
    def rows(self):
        return self.array.shape[0]
    @property
    def columns(self):
        return self.array.shape[1]
    
    def apply_operation(self, operation):
        """ Apply a MatrixOperation """
        operation.apply(self)

        

        
