#!/usr/bin/env python
from cmd import Cmd
from latex.latex_convertable import LatexConvertable
from termcolor import cprint

class MatrixCmd(Cmd):
    prompt = "matrixsh> "
    intro = """Welcome to the Matrix Shell!
    Manipulate matrices and translate them to LaTeX
    Type ? to list commands"""

    matrices = dict()

    def do_exit(self, inp):
        print("Bye")
        return True
    def help_exit(self):
        print("Exit the application")
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
        if not MatrixCmd.lower_count_check(args, count, message):
            return False
        if not MatrixCmd.upper_count_check(args, count, message):
            return False
        return True


    def read_matrix(self, name, rows, columns):
        """

        :name: identifier assigned to the matrix
        :rows: number of rows
        :columns: number of columns

        """
        raise NotImplementedError

    def do_read(self, line):
        inp = line.split()
        if not MatrixCmd.count_check(inp, 2):
            return
        name = inp[0].strip()
        if not name.isidentifier():
            cprint("The variable name must be a valid identifier", "red")
            return
        shape = inp[1].split('x')
        if not MatrixCmd.count_check(shape, 2, "Shape string must fit the format AxB"):
            return
        if not (shape[0].isdigit() and shape[1].isdigit()):
            cprint("Non-integers found", "red")
            return
        rows, columns = int(shape[0]), int(shape[1])

        """ Reading the matrix after all conditions are checked """
        self.read_matrix()

if __name__ == '__main__':
    MatrixCmd().cmdloop()
