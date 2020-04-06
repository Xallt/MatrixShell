from latex import begin_end, command

def matrix_to_latex(matrix, left = '(', right = ')'):
    """
    Convert a 2D array to a LaTeX string

    :matrix: 
    :left, right: brackets
    :returns: LaTeX string

    """
    array_str = ""
    for row in self.array:
        line = '&'.join([str(el) for el in row]) + "\\\\\n"
        array_str += line
    return \
        command("left" + self.left) + \
        begin_end(array_str, "array", 'c' * self.array.shape[1]).rstrip('\n') + \
        command("right" + self.right)

