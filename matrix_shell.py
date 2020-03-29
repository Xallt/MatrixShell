from cmd import Cmd
from LatexConvertable import LatexConvertable

class MatrixCmd(Cmd):
    prompt = 'matrixsh>'
    intro = """Welcome to the Matrix Shell!
    Manipulate matrices and translate them to LaTeX
    Type ? to list commands"""

    matrices = dict()

    def do_exit(self, inp):
        print("Bye")
        return True
    def help_exit(self):
        print("Exit the application")

if __name__ == '__main__':
    MatrixCmd().cmdloop()
