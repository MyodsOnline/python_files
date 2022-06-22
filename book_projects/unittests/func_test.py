import unittest
import os
import sys

parent_directory = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_directory)

from Bagels import get_clue

class TestClues(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_you_got_it(self):
        checked_answer = get_clue('324', '324')
        self.assertEqual(checked_answer, 'You got it!')

    def test_bagels(self):
        checked_answer = get_clue('601', '324')
        self.assertEqual(checked_answer, 'Bagels')

    def test_fermi(self):
        checked_answer = get_clue('621', '324')
        self.assertEqual(checked_answer, 'Fermi')

    def test_pico(self):
        checked_answer = get_clue('261', '324')
        self.assertEqual(checked_answer, 'Pico')

    def test_pico_fermi_pico(self):
        checked_answer = get_clue('423', '324')
        self.assertEqual(checked_answer, 'Pico Fermi Pico')


if __name__ == '__main__':
    unittest.main()
