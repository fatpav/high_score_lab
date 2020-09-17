import unittest

from src.high_scores import latest, personal_best, personal_top_three

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):

    def setUp(self):   
        self.scores = [34, 54, 765, 234, 1, 32, 764, 98, 901, 378, 811]
        self.scores_2 = [925, 925, 811, 734, 666]
        self.scores_3 = [925, 811]
        self.scores_4 = [1000]
    # Tests

    # Test latest score (the last thing in the list)
    def test_latest_score_on_the_list__811(self):
        self.assertEqual(811, latest(self.scores))

    # Test personal best (the highest score in the list)
    def test_for_the_highest_score_on_the_list__901(self):
        self.assertEqual(901, personal_best(self.scores))
    # Test top three from list of scores
    @unittest.skip("delete this line to run the test")
    def test_to_find_the_top_3_scores__901__811__765(self):
        self.assertEqual([901,811,765], personal_top_three(self.scores))
    # Test ordered from highest tp lowest
    @unittest.skip("delete this line to run the test")
    def test_to_order_scores_from_highest_to_lowest(self):
        self.assertEqual([901, 811, 765, 764, 378, 234, 98,54,34,32, 1], high_to_low(self.scores))
    # Test top three when there is a tie
    @unittest.skip("delete this line to run the test")
    def test_top_three_with_tied_scores(self):
        self.assertEqual(925, 925, 811, top_three(self.scores_2))
    # Test top three when there are less than three
    @unittest.skip("delete this line to run the test")
    def test_top_three_when_there_are_less_than_three_scores(self):
        self.assertEqual(925, 811, top_three(self.scores_3))
    # Test top three when there is only one
    @unittest.skip("delete this line to run the test")
    def test_for_top_three_with_only_one_score(self):
        self.assertEqual(1000, top_three(self.scores_4))
