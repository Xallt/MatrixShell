#!/usr/bin/env python
import numpy as np
from cmd import Cmd
from latex.convertion import matrix_to_latex
from termcolor import cprint
from pyperclip import copy
from typing import List, Optional

class MatrixShell(Cmd):
    prompt = "matrixsh> "
    intro = \
    "Welcome to the Matrix Shell!\n" \
    "Manipulate matrices and translate them to LaTeX\n" \
    "Type ? to list commands\n"

    matrices = dict()

    def __init__(self, stdin = None, stdout = None):
        Cmd.__init__(self, stdin = stdin, stdout = stdout)
        

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

    def lower_count_check(self, args: List[str], count: int, message: Optional[str] = None):
        """
        Checks if len(args) < count

        :args: argument list
        :count: required count

        """
        message = "Not enough arguments" if message is None else message
        if len(args) < count:
            raise ValueError(message)
    def upper_count_check(self, args: List[str], count: int, message: Optional[str] = None):
        """
        Check if len(args) > count

        :args: argument list
        :count: required count

        """
        message = "Too many arguments" if message is None else message
        if len(args) > count:
            raise ValueError(message)
    def count_check(self, args: List[str], count: int, message: Optional[str] = None):
        """
        Checks if len(args) == count

        :args: argument list
        :count: required count

        """
        self.lower_count_check(args, count, message)
        self.upper_count_check(args, count, message)

    def get_name(self, args: List[str], check_in_matrices: bool = True):
        """

        :args: command arguments
        :returns: (name, new args)

        """

        self.lower_count_check(args, 1)

        return (args[0], args[1:])
    def to_types(self, args: List[str], types: List[type]):
        """
        Check that arguments fit a particular type

        :args: elements to check
        :types: types to typecheck args for

        """

        self.count_check(args, len(types))
        result = []
        for i in range(len(args)):
            try:
                result.append(types[i](args[i]))
            except:
                raise ValueError("Expected type %s at argument %i" % (str(types[i]), i + 1))
        return result

    def read_matrix(self, name: str, rows: int, columns: int):
        """
        Read matrix from input line by line

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
        self.matrices[name] = np.array(matrix)
    def do_read(self, line):
        args = line.split()
        try:
            name, args = self.get_name(args, False)
            if not name.isidentifier():
                raise ValueError("The variable name must be a valid identifier")
            self.count_check(args, 1)
            shape = args[0].split('x')
            self.count_check(shape, 2, "Shape string must fit the format AxB")
            if not (shape[0].isdigit() and shape[1].isdigit()):
                raise ValueError("Non-integers in shape")
            shape = int(shape[0]), int(shape[1])
            assert shape[0] > 0 and shape[1] > 0, "Shape must be positive numbers"
        except ValueError as e:
            cprint(e, "red")
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

    def do_latex(self, line):
        name, args = self.get_name(line.split())
        self.count_check(args, 0)
        print(matrix_to_latex(self.matrices[name]))
    def help_latex(self):
        print(
            "latex NAME\n"
            "\tNAME - name of the matrix\n\n"
            "Print matrix converted to LaTeX\n"
        )

    def do_copy(self, line):
        name, args = self.get_name(line.split())
        self.count_check(args, 0)
        copy(matrix_to_latex(self.matrices[name]))
    def help_copy(self):
        print(
            "copy NAME\n"
            "\tNAME - name of the matrix\n\n"
            "Copy matrix converted to LaTeX\n"
        )

    def do_show(self, line):
        name, args = self.get_name(line.split())
        self.count_check(args, 0)
        for row in self.matrices[name]:
            print(("{:4}" * len(row)).format(*row))
    def help_show(self):
        print(
            "show NAME\n"
            "\tNAME - name of the matrix\n\n"
            "Show contents of the matrix\n"
        )

if __name__ == '__main__':
    MatrixShell().cmdloop()
