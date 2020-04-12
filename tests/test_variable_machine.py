import unittest
from variable_machine import VariableMachine

class TestVariableMachine(unittest.TestCase):

    """ Testing the variable machine """
    def setUp(self):
        self.machine = VariableMachine()

    def test_translation(self):
        self.assertEqual(
            self.machine.names_to_dict("a = b + c", "d"), 
            "d[a] = d[b] + d[c]"
        )
    def test_identifier(self):
        self.assertTrue(
            VariableMachine.is_identifier("abc123_ads")
        )
        self.assertFalse(
            VariableMachine.is_identifier("abc-dce+afs")
        )
    
