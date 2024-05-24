import unittest
import guessing_game


class TestGame(unittest.TestCase):

    def test1(self):
        guess = 5
        secret_number = 6
        result = guessing_game.check_guess(guess, secret_number)
        self.assertFalse(result)

    def test2(self):
        guess = 5
        secret_number = 5
        result = guessing_game.check_guess(guess, secret_number)
        self.assertTrue(result)


if __name__ == '__main__':

    unittest.main()
