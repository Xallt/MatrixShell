import re
from typing import Any

class VariableMachine:

    """ Custom variable controller """

    def __init__(self):
        self.var = dict()

    variable_regex = r"([a-zA-Z_][a-zA-Z_0-9]*)"

    @classmethod
    def is_identifier(cls, name: str) -> bool:
        """ Checks whether the given name is suitable for a variable name """

        return re.match("^" + cls.variable_regex + "$", name) is not None
    @classmethod
    def names_to_dict(cls, expression: str, dict_name: str) -> str:
        """ Replace variable names in expression with references to values in dict """

        return re.sub(cls.variable_regex, "%s[\"\\1\"]" % dict_name, expression)

    def eval(self, expression: str) -> Any:
        """ Evaluate the expression using the variables in this machine """

        return eval(VariableMachine.names_to_dict(expression, "self.var"))
    def assign(self, name: str, expression: str) -> None:
        """ Assign result of expression to a variable with a given name """

        self.var[name] = self.eval(expression)
    def get(self, name: str) -> Any:
        """ Get stored variable """

        return self.var[name]
        
