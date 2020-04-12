#!/usr/bin/env python
import numpy as np
from latex.convertion import matrix_to_latex
from prompter import Prompter
from termcolor import colored
from pyperclip import copy
from typing import List, Optional, Any
from fractions import Fraction

class MatrixShell(Prompter):

    matrices = dict()

    def __init__(self, stdin = None, stdout = None):
        super(MatrixShell, self).__init__(stdin = stdin, stdout = stdout)
        self.prompt = ">>> "
        self.intro = "Welcome to the Matrix Shell!\n"

    def read_matrix(self, name: str, rows: int, columns: int, elem_type: type = Fraction) -> None:
        """
        Read matrix from input line by line

        :name: identifier assigned to the matrix
        :rows: number of rows
        :columns: number of columns

        """
        matrix = []
        while len(matrix) < rows:
            try:
                if self.use_rawinput:
                    inp = input().split()
                else:
                    inp = self.stdin.readline().split()
            except EOFError:
                return

            try:
                row = list(map(elem_type, inp))
                assert len(row) == columns
            except:
                self.cprint("%s integers expected, try again" % columns, "red")
                continue
            matrix.append(row)
        self.matrices[name] = np.array(matrix)

    def on_prompt(self, line) -> bool:
        self.print("Processed " + line)

    def show_matrix(self, line):
        name, args = self.get_name(line.split())
        self.count_check(args, 0)
        max_len = 0
        for row in self.matrices[name]:
            for elem in row:
                max_len = max(max_len, len(str(elem)))
        max_len += 1
        for row in self.matrices[name]:
           self.print(("{:4}" * len(row)).format(*row))

if __name__ == '__main__':
    MatrixShell().cmdloop()
