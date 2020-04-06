from latex import begin_end, command

def matrix_to_latex(matrix, left = '(', right = ')'):
    """
    Convert a 2D array to a LaTeX string

    :matrix: 2D rectangular array
    :left, right: brackets
    :returns: LaTeX string

    """
    rows = len(matrix)
    lines = []
    for row in matrix:
        lines.append(
            '&'.join([str(el) for el in row]) + r"\\"
        )
    return \
        command("left" + left) + \
        begin_end(
            '\n'.join(lines), 
            "array", 
            'c' * matrix.shape[1]
        ).rstrip('\n') + \
        command("right" + right)

