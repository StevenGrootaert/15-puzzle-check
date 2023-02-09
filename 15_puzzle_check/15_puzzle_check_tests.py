import unittest
import _15_puzzle_check
 
class Test__15_puzzle_check_tests(unittest.TestCase):
    def test_find_incoming_parity(self):
        self.assertEqual(incoming.index(16), 16)
        self.fail("Not implemented")

if __name__ == '__main__':
    unittest.main()

incoming = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

Test__15_puzzle_check_tests.test_find_incoming_parity(incoming)

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