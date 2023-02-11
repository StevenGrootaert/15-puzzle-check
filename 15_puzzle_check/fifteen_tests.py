import unittest
import fifteen
#import _15_puzzle_check 
#from _15_puzzle_check import find_incoming_parity
 
#1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

class Test_fifteen(unittest.TestCase):
    def test_assert_valid_input(self):
        SHOULD_BE_VALID = True
        SHOULD_BE_INVALID = False
        tests = [
            [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],SHOULD_BE_VALID],
            [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 47],SHOULD_BE_INVALID]
        ]
        for test_input,should_be_valid in tests:
            if should_be_valid == SHOULD_BE_VALID:
                fifteen.assert_valid_input(test_input,set(test_input))
            elif should_be_valid == SHOULD_BE_INVALID:
                had_exception = False
                try:
                    fifteen.assert_valid_input(test_input,set(test_input))
                except:
                    had_exception = True
                self.assertTrue(had_exception)

    def test_solvable(self):
        self.assertFalse(fifteen.solvable("ODD", 2))
        self.assertTrue(fifteen.solvable("EVEN", 2))


if __name__ == '__main__':
    unittest.main()

#incoming = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

'''
every statement that should have a test. 
every function I have is dependant on the input set/list ... 
-- this is feeling more and more like it should be a class if I can test the input
and have a set of various Boards and Tiles to test 
def get_inputs 
    def test_length(self):
        board_1 = Board(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
        board_2 = Board(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
        self.assertEqual(len(board_1), 16)
        self.assertEqual(len(board_2), 15)

    def test_find_duplications(self):
        board_3 = Board(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 15)
        self.assertEqual(dups(15), 15) ?? 
        

    def test_range(self):
        tile_1 = 16
        tile_2 = 0
        tile_3 = 20
        tile_4 = 6
'''

'''
test cases for various inputs
missing space, too few tiles
    incoming = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

missing space, tile outside of range, correct number of tiles
    incoming = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18]

missing space, duplicate tile, correct number of tiles
    incoming = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 15]

missing space, multiple duplicate tiles, correct number of tiles
    incoming = [1, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

this could go on for a while with every combination...
too many tiles, duplicate tiles in and out of range, has space
    incoming = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 11, 12, 13, 14, 15, 16, 20, 20, 24]

too few tiles, duplicate tiles in and out of range, has space, missing tiles
    incoming = [1, 3, 6, 9, 10, 10, 10, 11, 12, 16, 20, 20, 24]

too few tiles, duplicate tiles in and out of range, missing space
    incoming = [0, 1, 2, 3, 8, 9, 10, 10, 10, 11, 20, 20, 24]


test cases for solvable - given a valid incoming input::
parity EVEN, transpositions even (6), solvable
    #incoming=[1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16]

parity EVEN, transpositions odd (7), NOT solvable
    #incoming=[15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 16]

parity ODD, transpositions odd (11), solvable
    #incoming=[7, 8, 9, 10, 6, 1, 2, 11, 5, 4, 3, 12, 16, 15, 14, 13]

parity ODD, transpositions even (10), NOT solvable
    #incoming=[1, 8, 9, 16, 2, 7, 10, 15, 3, 6, 11, 14, 4, 5, 12, 13]

'''