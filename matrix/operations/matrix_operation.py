class MatrixOperation(LatexConvertable):

    """ Interface for primitive matrix operations """

    def __init__(self):
        pass

    def to_latex(self):
        """ Assumes the subclass has __str__ implemented giving some LaTeX representation """
        return r"\xrightarrow{%s}" % str(self)

    def apply(self, matrix):
        """ Apply this operation to a matrix """

