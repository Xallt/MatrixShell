import unittest
import numpy
from matrix.operations.primitives import MultiplyRow, SwapRows, AddRowToRow

class TestPrimitiveOperation(unittest.TestCase):

    """ Parent class for all primitive operation testcases """

    def setUp(self):
        """ Initialize a readable matrix to work with """
        self.matrix = numpy.arange(25).reshape((5, 5)) + 1
    def applied(self, *operations):
        mat = numpy.copy(self.matrix)
        for op in operations:
            if op is not None:
                op.apply(mat)
        return mat
    def assertMatrixEqual(self, mat1, mat2):
        self.assertTrue(numpy.equal(mat1, mat2).all())

class TestMultiplyRow(TestPrimitiveOperation):

    def test_multiply_by_zero(self):
        self.assertRaises(AssertionError, MultiplyRow, 0, 0)

    def test_multiply_static(self):
        op = MultiplyRow(3, -1)
        matrix2 = self.applied(op, op)
        self.assertMatrixEqual(
            self.matrix,
            self.applied(op, op)
        )

    def test_multiply_same(self):
        op = MultiplyRow(2, 5)
        self.assertMatrixEqual(
            self.applied(op),
            self.applied(op)
        )
    def test_some_multiply(self):
        op = MultiplyRow(1, -7)
        mat = self.applied(op)
        self.matrix[1] *= -7
        self.assertMatrixEqual(self.matrix, mat)

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

if __name__ == "__main__":
    unittest.main()
