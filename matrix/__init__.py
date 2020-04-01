import numpy
from latex.latex_convertable import LatexConvertable
from latex import begin_end, command

class Matrix(LatexConvertable):

    """ numpy.array wrapper for common operations """

    def __init__(self, matrix, left = '(', right = ')'):
        self.array = numpy.array(matrix)
        self.left = left
        self.right = right

    @property
    def rows(self):
        return self.array.shape[0]
    @property
    def columns(self):
        return self.array.shape[1]
    
    def apply_operation(self, operation):
        """ Apply a MatrixOperation """
        operation.apply(self)

    def to_latex(self):
        array_str = ""
        for row in self.array:
            line = '&'.join([str(el) for el in row]) + "\\\\\n"
            array_str += line
        return \
            command("left" + self.left) + \
            begin_end(array_str, "array", 'c' * self.array.shape[1]).rstrip('\n') + \
            command("right" + self.right)

