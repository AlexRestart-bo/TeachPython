import run
import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(unittest.TestCase):

    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runner1 = Runner('usein', 10)
        self.runner2 = Runner('andrey', 9)
        self.runner3 = Runner('nick', 3)

    @classmethod
    def tearDownClass(cls):
        for key in cls.all_results.keys():
            print("zero")
            print(cls.all_results[key])
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour1(self):
        tour1 = Tournament(90, self.runner1, self.runner3)
        medals = tour1.start()
        self.all_results.update({1: medals})
        self.assertEquals(medals[2], 'nick')
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour2(self):
        tour2 = Tournament(90, self.runner2, self.runner3)
        medals = tour2.start()
        self.all_results.update({1: medals})
        self.assertEquals(medals[2], 'nick')
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tour3(self):
        tour3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        medals = tour3.start()
        self.all_results.update({1: medals})
        self.assertEquals(medals[3], 'nick')

class RunnerTest(unittest.TestCase):
    is_frozen = False
    def setUp(self):
        print("setup")
    @classmethod
    def setUpClass(cls):
        print("MegaSetup")
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        num_run = run.Runner('obj1')
        for _ in range(10):
            num_run.walk()
        self.assertEquals(num_run.distance, 50)
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        new_run = run.Runner('obj2')
        for _ in range(10):
            new_run.run()
        self.assertEquals(new_run.distance, 100)
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        ch1 = run.Runner('challenge1')
        ch2 = run.Runner('challenge2')
        for _ in range(10):
            ch1.run()
            ch2.walk()
        self.assertEquals(ch1.distance, ch2.distance)

if __name__ == '__main__':
    unittest.main()