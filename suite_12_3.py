import unittest
from test_12_3 import RunnerTest
from test_12_3 import TournamentTest

my_suite_test = unittest.TestSuite()
my_suite_test.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))
my_suite_test.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
my_runner = unittest.TextTestRunner(verbosity=2)
my_runner.run(my_suite_test)

