import unittest

from src.high_scores import latest, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):

    def setUp(self):   
        self.scores = [34, 54, 765, 234, 1, 32, 764, 98, 901, 378, 811]

    # Tests

    # Test latest score (the last thing in the list)
    def test_latest_score_on_the_list__811(self):
        self.assertEqual(811, latest(self.scores))

    # Test personal best (the highest score in the list)
    def test_for_the_highest_score_on_the_list__901(self):
        self.assertEqual(901, personal_best(self.scores))
    # Test top three from list of scores

    # Test ordered from highest tp lowest

    # Test top three when there is a tie

    # Test top three when there are less than three

    # Test top three when there is only one
