import unittest
import fifteen

class Test_fifteen(unittest.TestCase):
    def test_assert_valid_input(self):
        SHOULD_BE_VALID = True
        SHOULD_BE_INVALID = False
        tests = [
            [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],SHOULD_BE_VALID],
            [[16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],SHOULD_BE_VALID],
            [[0, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],SHOULD_BE_INVALID],
            [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 47],SHOULD_BE_INVALID],
            [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],SHOULD_BE_INVALID],
            [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 15],SHOULD_BE_INVALID],
            [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11, 12, 13, 14, 15, 16, 20, 20, 24], SHOULD_BE_INVALID],
            [[1, 3, 6, 9, 10, 10, 10, 11, 12, 16, 20, 20, 24],SHOULD_BE_INVALID]
        ]
        for test_input,test_valid in tests:
            if test_valid == SHOULD_BE_VALID:
                fifteen.assert_valid_input(test_input,set(test_input))
            elif test_valid == SHOULD_BE_INVALID:
                had_exception = False
                try:
                    fifteen.assert_valid_input(test_input,set(test_input))
                except:
                    had_exception = True
                self.assertTrue(had_exception)

    def test_find_duplications(self):
        tests = [
            [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 16], {16}],
            [[10, 11, 12, 12, 13, 14, 16, 16], {12, 16}],
            [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 16, 18, 18, 37, 42, 42], {16, 18, 42}],
            [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 14, 15, 16], {10}],
            [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 14, 20, 20], {10, 20}],
            [[1, 2, 2, 4, 4, 6, 7, 8, 9, 10, 11, 12, 12, 14, 16, 16], {2, 4, 12, 16}]
        ]
        for test_list, test_exp_dups in tests:
            test_set = set(test_list)
            self.assertEqual(fifteen.find_duplications(test_list, test_set), test_exp_dups)

    def test_find_incoming_parity(self):
        tests = [
            [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 16], 'EVEN'],
            [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 16, 1], 'ODD'],
            [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 16, 1, 1], 'EVEN'],
            [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 16, 1, 1, 1], 'ODD'],
            [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 16, 1, 1, 1, 1], 'ODD'],
            [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 16, 1, 1, 1, 1, 1], 'EVEN'],
            [[1, 1, 1, 1, 1, 1, 1, 1, 1, 16, 1, 1, 1, 1, 1, 1], 'ODD'],
            [[1, 1, 1, 1, 1, 1, 1, 1, 16, 1, 1, 1, 1, 1, 1, 1], 'EVEN'],
            [[1, 1, 1, 1, 1, 1, 1, 16, 1, 1, 1, 1, 1, 1, 1, 1], 'EVEN'],
            [[1, 1, 1, 1, 1, 1, 16, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'ODD'],
            [[1, 1, 1, 1, 1, 16, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'EVEN'],
            [[1, 1, 1, 1, 16, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'ODD'],
            [[1, 1, 1, 16, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'ODD'],
            [[1, 1, 16, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'EVEN'],
            [[1, 16, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'ODD'],
            [[16, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 'EVEN'],
        ]
        for test_incoming, test_parity in tests:
            if test_parity == 'EVEN':
                self.assertEqual((fifteen.find_incoming_parity(test_incoming)),'EVEN')
            elif test_parity == 'ODD':
                self.assertEqual(fifteen.find_incoming_parity(test_incoming),'ODD')

    def test_find_incoming_transpositions(self): 
        tests = [
            [[1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16], 6],
            [[15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16], 7],
            [[7, 8, 9, 10, 6, 1, 2, 11, 5, 4, 3, 12, 16, 15, 14, 13], 11],
            [[1, 8, 9, 16, 2, 7, 10, 15, 3, 6, 11, 14, 4, 5, 12, 13], 10]
        ]
        for test_incoming, expect_tran in tests:
            self.assertEqual(fifteen.find_incoming_transpositions(test_incoming), expect_tran)

        #test_1 = [1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16]
        #test_tran_1 = 6
        #if (fifteen.find_incoming_transpositions(test_1)) != (test_tran_1):
        #    self.fail("incorrect numbr of transpositions")

    def test_check_solvable(self):
        self.assertTrue(fifteen.check_solvable("EVEN", 2))
        self.assertFalse(fifteen.check_solvable("EVEN", 3))
        self.assertTrue(fifteen.check_solvable("ODD", 3))
        self.assertFalse(fifteen.check_solvable("ODD", 2))

if __name__ == '__main__':
    unittest.main()
