from latex.latex_convertable import LatexConvertable
from matrix.operations.matrix_operation import MatrixOperation

class MultiplyRow(MatrixOperation):

    """ Primitive operation for multiplying a row of a matrix by a constant """

    def __init__(self, row, koefficient):
        assert koefficient != 0, "The multiplying koefficient must be non-zero"
        self.row = row
        self.koefficient = koefficient

    def apply(self, matrix):
        matrix[self.row] *= self.koefficient
    def to_latex(self):
        return r"(%s) \to %s\cdot(%s)" % (self.row + 1, self.koefficient, self.row + 1)

class SwapRows(MatrixOperation):

    """ Primitive operation for swapping to rows of a matrix """

    def __init__(self, row1, row2):
        self.row1 = row1
        self.row2 = row2

    def apply(self, matrix):
        matrix[[self.row1, self.row2]] = matrix[[self.row2, self.row1]]
    def to_latex(self):
        return r"(%s) \leftrightarrow (%s)" % (self.row1 + 1, self.row2 + 1)

class AddRowToRow(MatrixOperation):

    """ Primitive operation for adding one row multiplied by a constant to another """

    def __init__(self, row1, row2, koefficient):
        assert row1 != row2, "Cant row to itself"
        self.row1 = row1
        self.row2 = row2
        self.koefficient = koefficient

    def apply(self, matrix):
        matrix[self.row2] += matrix[self.row1] * self.koefficient
    def to_latex(self):
        return r"(%s) \to (%s) + %s\cdot(%s)" % (self.row2 + 1, self.row2 + 1, self.koefficient, self.row1 + 1)
