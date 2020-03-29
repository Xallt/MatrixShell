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

    def to_latex(self):
        wrap = "\\begin{{pmatrix}}\n{}\\end{{pmatrix}}"
        lines = []
        for row in self.array:
            line = ""
            for i in range(len(row)):
                if i == 0:
                    line += str(row[i])
                else:
                    # if i >= cols:
                        # line += "&\\aug"
                    line += "&" + str(row[i])
            lines.append(line)
        return wrap.format('\\\\\n'.join(lines) + '\n')
