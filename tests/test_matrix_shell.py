import unittest
from matrix_shell import MatrixShell
import io

class TestMatrixShell(unittest.TestCase):

    """Testing MatrixShell commands"""

    def get_response_lines(self, lines):
        lines.append("exit")
        file_in = io.StringIO('\n'.join(lines) + '\n')
        file_out = io.StringIO()
        m = MatrixShell(stdin = file_in, stdout = file_out)
        m.cmdloop()
        out_s = file_out.getvalue()
        out_s = ' '.join(out_s[len(m.intro):].split(m.prompt)[:-1])
        return out_s.strip('\n ').split('\n')

    def test_show(self):
        lines = [
            "read a 2x2",
            "1 2",
            "3 4",
            "show a"
        ]
        show_mat = self.get_response_lines(lines)
        show_mat = [line.replace('\t', '').split() for line in show_mat]
        self.assertEqual(show_mat, [["1", "2"], ["3", "4"]])
    def test_latex(self):
        lines = [
            "read a 2x2",
            "4 3",
            "2 1",
            "latex a"
        ]
        latex_mat = self.get_response_lines(lines)
        self.assertEqual(
            '\n'.join(latex_mat) + '\n',
            "\\left(\\begin{array}[cc]\n"
            "4&3\\\\\n"
            "2&1\\\\\n"
            "\\end{array}\\right)\n"
        )
    
if __name__ == "__main__":
    unittest.main()
