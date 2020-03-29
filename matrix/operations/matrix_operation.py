from latex.latex_convertable import LatexConvertable

class MatrixOperation(LatexConvertable):

    """ Interface for primitive matrix operations """

    def __init__(self):
        pass

    def apply(self, matrix):
        """ Apply this operation to a matrix """
        raise NotImplementedError
