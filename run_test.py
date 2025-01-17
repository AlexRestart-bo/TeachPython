import run
import unittest


class RunnerTest(unittest.TestCase):

    def setUp(self):
        print("setup")
    @classmethod
    def setUpClass(cls):
        print("MegaSetup")

    def test_walk(self):
        num_run = run.Runner('obj1')
        for _ in range(10):
            num_run.walk()
        self.assertEquals(num_run.distance, 50)
    def test_run(self):
        new_run = run.Runner('obj2')
        for _ in range(10):
            new_run.run()
        self.assertEquals(new_run.distance, 100)
    def test_challenge(self):
        ch1 = run.Runner('challenge1')
        ch2 = run.Runner('challenge2')
        for _ in range(10):
            ch1.run()
            ch2.walk()
        self.assertEquals(ch1.distance, ch2.distance)

if __name__ == '__main__':
    unittest.main()