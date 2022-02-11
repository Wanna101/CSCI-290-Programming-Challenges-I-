import unittest
from knights import handleInput

# David Young
# Basic testing of cases for the nine knights week4 kattis code
# Run this using `python3 test_knights.py`
#
# NOTE: unittest is directory (package) sensitive, so the location of this file relative to the subject & the directory from which you run it are important

class GenericTester(unittest.TestCase):
	def run_cases(self, cases):
		for case in cases:
                        actual = handleInput(case[0])
                        self.assertEqual(actual, case[1], "For this board:\n%s\n***** Expected '%s' but got '%s' ***** " % (case[0], case[1], actual))

	def test_knight1(self):
            c1 = """...k.
...k.
k.k..
.k.k.
k.k.k"""
            data1 = c1.split("\n")
            o1 = "invalid"
            cases = [ (data1, o1) ]
            self.run_cases(cases)

	def test_knight2(self):
            c1 = """.....
...k.
k.k.k
.k.k.
k.k.k"""
            data1 = c1.split("\n")
            o1 = "valid"
            cases = [ (data1, o1) ]
            self.run_cases(cases)

	def test_knight3(self):
            c1 = """.....
...k.
k.k.k
.k.k.
k...k"""
            data1 = c1.split("\n")
            o1 = "invalid"
            cases = [ (data1, o1) ]
            self.run_cases(cases)

if __name__ == '__main__':
    unittest.main()
