import numpy

class Matrix(LatexConvertable):

    """ numpy.array wrapper for common operations """

    def __init__(self, rows, columns):
        self.array = numpy.zeros((rows, columns))

    @property
    def rows(self):
        return self.array.shape[0]
    @property
    def columns(self):
        return self.array.shape[1]
    
    def apply_operation(self, operation):
        """ Apply a MatrixOperation """
        operation.apply(self)

        

        
