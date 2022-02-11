import unittest
from grandpa_checkerboard import handleInput

# David Young
# Basic testing of cases for the grandpa checkerboard week4 kattis code
# Run this using `python3 test_grandpa_checkerboard.py`
#
# NOTE: unittest is directory (package) sensitive, so the location of this file relative to the subject & the directory from which you run it are important

class GenericTester(unittest.TestCase):
	def run_cases(self, cases):
		for case in cases:
                        actual = handleInput(case[0], case[1])
                        self.assertEqual(actual, case[2], "For this board:\n%s\n***** Expected '%s' but got '%s' ***** " % (case[0], case[2], actual))

	def test_gpa1(self):
            c1 = """4
WBBW
WBWB
BWWB
BWBW"""
            data1 = c1.split("\n")
            del data1[0]
            sizeboard = len(data1) 
            o1 = "1"
            cases = [ (data1, sizeboard, o1) ]
            self.run_cases(cases)

	def test_gpa2(self):
            c1 = """4
BWWB
BWBB
WBBW
WBWW"""
            data1 = c1.split("\n")
            del data1[0]
            sizeboard = len(data1) 
            o1 = "0"
            cases = [ (data1, sizeboard, o1) ]
            self.run_cases(cases)

	def test_gpa3(self):
            c1 = """6
BWBWWB
WBWBWB
WBBWBW
BBWBWW
BWWBBW
WWBWBB"""
            data1 = c1.split("\n")
            del data1[0]
            sizeboard = len(data1) 
            o1 = "0"
            cases = [ (data1, sizeboard, o1) ]
            self.run_cases(cases)

	def test_gpa4(self):
            c1 = """6
WWBBWB
BBWWBW
WBWBWB
BWBWBW
BWBBWW
WBWWBB"""
            data1 = c1.split("\n")
            del data1[0]
            sizeboard = len(data1) 
            o1 = "1"
            cases = [ (data1, sizeboard, o1) ]
            self.run_cases(cases)

if __name__ == '__main__':
    unittest.main()
