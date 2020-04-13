import unittest
from variable_machine import VariableMachine

class TestVariableMachine(unittest.TestCase):

    """ Testing the variable machine """
    def setUp(self):
        self.machine = VariableMachine()

    def test_translation(self):
        self.assertEqual(
            self.machine.names_to_dict("a - b + c", ["a", "b"], "d"), 
            "d[\"a\"] - d[\"b\"] + c"
        )
    def test_identifier(self):
        self.assertTrue(
            VariableMachine.is_identifier("abc123_ads")
        )
        self.assertFalse(
            VariableMachine.is_identifier("abc-dce+afs")
        )
    def test_assign(self):
        self.machine.assign("a", "1")
        self.assertEqual(self.machine.get("a"), 1)

        self.machine.assign("a", "1 + 1 + 1 + 2 * 0")
        self.machine.assign("a", "a * 2 + 2 ** a-1")
        self.assertEqual(self.machine.get("a"), 3 * 2 + 2 ** 3 - 1)
    
