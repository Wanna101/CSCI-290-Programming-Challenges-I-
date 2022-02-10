import unittest
from targets import handleInput

# Run this using `python3 fizzbuzz.test.py`
# OR
# python -m unittest
#
# NOTE: unittest is directory (package) sensitive, so the location of this file relative to the subject & the directory from which you run it are important

class GenericTester(unittest.TestCase):
	def run_cases(self, cases):
		for case in cases:
			actual = handleInput(case[0])
			self.assertEqual(actual, case[1], "Expected %s" % actual)

	def test_input(self):
            c1 = """3
rectangle 1 1 10 5
circle 5 0 8
rectangle -5 3 5 8
5
1 1
4 5
10 10
-10 -1
4 -3
"""
            data1 = c1.split("\n")
            o1 = """2
3
0
0
1
"""
            cases = [ (data1, o1) ]
            self.run_cases(cases)

if __name__ == '__main__':
    unittest.main()
