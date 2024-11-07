import unittest
from math_quiz import get_random_integer, get_random_operator, generate_math_problem


class TestMathGame(unittest.TestCase):

    def test_get_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_random_operator(self):
        # Test if random operator generated is one of the specified operators
        operators = ['+', '-', '*']
        for _ in range(1000):
            rand_operator = get_random_operator()
            self.assertIn(rand_operator, operators)
    def test_generate_math_problem(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (3, 4, '-', '3 - 4', -1),
                (2, 3, '*', '2 * 3', 6),
                (5, 2, '*', '5 * 2', 10),
                (10, 3, '+', '10 + 3', 13),
                (10, 3, '-', '10 - 3', 7),
                (10, 3, '*', '10 * 3', 30)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # Test the generated problem and answer
                problem, answer = generate_math_problem(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)
if __name__ == "__main__":
    unittest.main()
