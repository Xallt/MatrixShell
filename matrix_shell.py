#!/usr/bin/env python
from cmd import Cmd
from latex.latex_convertable import LatexConvertable
from matrix import Matrix
from termcolor import cprint

class MatrixShell(Cmd):
    prompt = "matrixsh> "
    intro = \
    "Welcome to the Matrix Shell!\n" \
    "Manipulate matrices and translate them to LaTeX\n" \
    "Type ? to list commands\n"

    matrices = dict()

    def do_exit(self, inp):
        print("Bye")
        return True
    def help_exit(self):
        print(
            "exit\n\n"
            "Exit the application\n",
            sep = '\n'
        )
    do_EOF = do_exit
    help_EOF = help_exit

    @staticmethod
    def lower_count_check(args, count, message = None):
        """

        :args: argument list
        :count: required count
        :returns: True if len(args) < count, prints an error and returns False otherwise

        """
        if message is None:
            message = "Not enough arguments"
        if len(args) < count:
            cprint(message, "red")
            return False
        return True
    @staticmethod
    def upper_count_check(args, count, message = None):
        """

        :args: argument list
        :count: required count
        :message: the error message
        :returns: True if len(args) > count, prints an error and returns False otherwise

        """
        if message is None:
            message = "Too many arguments"
        if len(args) > count:
            cprint(message, "red")
            return False
        return True
    @staticmethod
    def count_check(args, count, message = None):
        """

        :args: argument list
        :count: required count
        :returns: True if len(args) == count, prints an error and returns False otherwise

        """
        if not MatrixShell.lower_count_check(args, count, message):
            return False
        if not MatrixShell.upper_count_check(args, count, message):
            return False
        return True


    def read_matrix(self, name, rows, columns):
        """

        :name: identifier assigned to the matrix
        :rows: number of rows
        :columns: number of columns

        """
        matrix = []
        while len(matrix) < rows:
            try:
                inp = input().split()
            except EOFError:
                return

            try:
                row = list(map(int, inp))
                assert len(row) == columns
            except:
                cprint("%s integers expected, try again" % columns, "red")
                continue
            matrix.append(row)
        self.matrices[name] = Matrix(matrix)

    def do_read(self, line):
        inp = line.split()
        if not MatrixShell.count_check(inp, 2):
            return
        name = inp[0].strip()
        if not name.isidentifier():
            cprint("The variable name must be a valid identifier", "red")
            return
        shape = inp[1].split('x')
        if not MatrixShell.count_check(shape, 2, "Shape string must fit the format AxB"):
            return
        if not (shape[0].isdigit() and shape[1].isdigit()):
            cprint("Non-integers found", "red")
            return
        rows, columns = int(shape[0]), int(shape[1])

        """ Reading the matrix after all conditions are checked """
        self.read_matrix(name, rows, columns)
    def help_read(self):
        print(
            "read NAME AxB\n"
            "\tNAME - name of the matrix (valid python identifier)\n"
            "\tA, B - matrix rows and columns\n\n"
            "Read the matrix from input\n"
        )

    def do_latex(self, name):
        if not MatrixShell.count_check(name.split(), 1):
            return
        print(self.matrices[name].to_latex())
    def help_latex(self):
        print(
            "latex NAME\n"
            "\tNAME - name of the matrix\n\n"
            "Print matrix converted to LaTeX\n"
        )

if __name__ == '__main__':
    MatrixShell().cmdloop()
