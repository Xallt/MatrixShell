def command(command, curly = None, square = None):
    """

    :command: command name
    :curly_param: {curly_param}
    :square_param: [square_param]
    :returns: LaTeX string

    """

    curly_str = "" if param is None else "{%s}" % curly
    square_str = "" if param is None else "[%s]" % square
    return r"\%s%s%s" % (command, curly_str, square_str)

def begin_end(block, block_type, param = None):
    """

    :block: Block of LaTeX to put inside \\begin ... \\end
    :block_type: Block type (\\begin{block_type} ...)
    :param: parameter (\\begin{...}[param])
    :returns: Result LaTeX string

    """
    lines = block.strip('\n').split('\n')
    lines = ['\t' + line for line in lines]
    return \
        command("begin", block_type, param) + '\n' + \
        '\n'.join(lines) + '\n' + \
        command("end", block_type)  + '\n'
