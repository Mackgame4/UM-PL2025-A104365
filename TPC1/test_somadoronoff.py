import unittest
from io import StringIO
import sys

# Import the function to test
from somadoronoff import somadoronoff

class TestSomadorOnOff(unittest.TestCase):
    def setUp(self):
        self.original_stdout = sys.stdout
        sys.stdout = StringIO() # Capture print output

    def tearDown(self):
        sys.stdout = self.original_stdout # Restore original stdout

    def get_output(self):
        return sys.stdout.getvalue().strip()

    def test_case_1(self):
        """Test expected behavior for given input sequence."""
        global isOn, soma
        isOn = True  # Reset global state
        soma = 0
        test_input = [
            "Hoje, 7 de Fevereiro de 2025, o professor de Processamento de Linguagens"
            "deu-nos"
            "este trabalho para fazer.=OfF"
            "E deu-nos 7="
            "dias para o fazer... ON"
            "Cada trabalho destes vale 0.25 valores da nota final!="
        ]
        expected_output = ">> 2032\n>> 2032\n>> 2057"
        for line in test_input:
            somadoronoff(line.lower())
        self.assertEqual(self.get_output(), expected_output)

if __name__ == "__main__":
    unittest.main()