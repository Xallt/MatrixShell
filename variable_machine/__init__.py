import re

class VariableMachine:

    """ Custom variable controller """

    def __init__(self):
        self.var = dict()

    variable_regex = r"([a-zA-Z_][a-zA-Z_0-9]*)"

    @classmethod
    def is_identifier(cls, name):
        """ Checks whether the given name is suitable for a variable name """
        return re.match(name, "$" + cls.variable_regex + "^")

    def names_to_dict(self, expression: str, dict_name: str) -> str:
        """ Replace variable names in expression with references to values in dict """
        self.
        return re.sub(self.variable_regex, r"%s[\1]" % dict_name, expression)

    def assign(self, name, expression):
        """ Assign result of expression to a variable with a given name """
        raise NotImplementedError

        
