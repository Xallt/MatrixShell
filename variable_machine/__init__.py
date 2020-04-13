import re
from typing import Any, List

class VariableMachine:

    """ Custom variable controller """

    def __init__(self):
        self.var = dict()

    @classmethod
    def is_identifier(cls, name: str) -> bool:
        """ Checks whether the given name is suitable for a variable name """

        return re.match(r"^[a-zA-Z_][a-zA-Z_0-9]*$", name) is not None

    @classmethod
    def names_to_dict(cls, expression: str, names: List[str], dict_name: str) -> str:
        """ Replace variable names in expression with references to values in dict """
        if len(names) == 0:
            return expression
        pattern = r"(?!<=[a-zA-Z_0-9])(%s)(?!=[a-zA-Z_0-9])" % '|'.join(names)
        return re.sub(pattern, "%s[\"\\1\"]" % dict_name, expression)

    def names(self):
        """ Return list of assigned variable names """
        return self.var.keys()
    def eval(self, expression: str) -> Any:
        """ Evaluate the expression using the variables in this machine """
        processed_expression = VariableMachine.names_to_dict(expression, self.names(), "self.var")
        return eval(processed_expression)
    def assign(self, name: str, expression: str) -> None:
        """ Assign result of expression to a variable with a given name """
        if not VariableMachine.is_identifier(name):
            raise ValueError("name '%s' is not a valid identifier" % name)
        self.var[name] = self.eval(expression)
    def get(self, name: str) -> Any:
        """ Get stored variable """
        if not name in self.var:
            raise NameError("name '%s' is not defined in current VariableMachine")

        return self.var[name]
        
