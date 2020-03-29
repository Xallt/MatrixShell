import unittest
import numpy
from matrix.operations.primitives import MultiplyRow, SwapRows, AddRowToRow

class TestPrimitiveOperation(unittest.TestCase):

    """ Parent class for all primitive operation testcases """

    def setUp(self):
        """ Initialize a readable matrix to work with """
        self.matrix = numpy.arange(25).reshape((5, 5)) + 1

    def applied(self, *operations):
        """ Return a copy of self.matrix with operations applied to it """
        mat = numpy.copy(self.matrix)
        for op in operations:
            if op is not None:
                op.apply(mat)
        return mat

    def assertMatrixEqual(self, mat1, mat2, msg=None):
        self.assertTrue(numpy.equal(mat1, mat2).all(), None)

class TestMultiplyRow(TestPrimitiveOperation):

    def test_multiply_by_zero(self):
        with self.assertRaises(AssertionError, msg =  "Multiplying a row by 0 should not be possible"):
            MultiplyRow(0, 0)

    def test_multiply_static(self):
        op = MultiplyRow(3, -1)
        matrix2 = self.applied(op, op)
        self.assertMatrixEqual(
            self.matrix,
            self.applied(op, op),
            "Multiplying a row by -1 twice should not change anything"
        )

    def test_some_multiply(self):
        op = MultiplyRow(1, -7)
        mat = self.applied(op)
        self.matrix[1] *= -7
        self.assertMatrixEqual(
            self.matrix, 
            mat, 
            "Operation produced wrong result"
        )

    def test_latex(self):
        op = MultiplyRow(4, -27)
        self.assertEqual(
            r"(5) \to -27\cdot(5)",
            op.to_latex()
        )

class TestSwapRows(TestPrimitiveOperation):

    def test_same_row(self):
        op = SwapRows(3, 3)
        self.assertMatrixEqual(
            self.matrix,
            self.applied(op)
        )
    def test_double_swap(self):
        op = SwapRows(1, 4)
        opr = SwapRows(4, 1)
        self.assertMatrixEqual(
            self.matrix,
            self.applied(op, op)
        )
        self.assertMatrixEqual(
            self.matrix,
            self.applied(op, opr)
        )
    def test_some_swap(self):
        op = SwapRows(3, 1)
        mat = self.applied(op)
        self.matrix[[1, 3]] = self.matrix[[3, 1]]
        self.assertMatrixEqual(
            self.matrix,
            mat
        )

    def test_latex(self):
        op = SwapRows(4, 2)
        self.assertIn(
            op.to_latex(),
            [
                r"(5) \leftrightarrow (3)",
                r"(3) \leftrightarrow (5)",
            ]
        )

class TestAddRowToRow(TestPrimitiveOperation):

    def test_same_row(self):
        self.assertRaises(AssertionError, AddRowToRow, 3, 3, 5)

    def test_inverse_add(self):
        op = AddRowToRow(1, 4, 3)
        opr = AddRowToRow(1, 4, -3)
        self.assertMatrixEqual(
            self.matrix,
            self.applied(op, opr)
        )
        self.assertMatrixEqual(
            self.matrix,
            self.applied(opr, op)
        )

    def test_zero_koef(self):
        op = AddRowToRow(4, 1, 0)
        self.assertMatrixEqual(
            self.matrix,
            self.applied(op)
        )

    def test_latex(self):
        op = AddRowToRow(4, 0, 13)
        self.assertEqual(
            op.to_latex(),
            r"(1) \to (1) + 13\cdot(5)"
        )


if __name__ == "__main__":
    unittest.main()
