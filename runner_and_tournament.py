import unittest
from unittest import TestCase


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

class TournamentTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('usein', 10)
        self.runner2 = Runner('andrey', 9)
        self.runner3 = Runner('nick', 3)

    @classmethod
    def tearDownClass(cls):
        for key in cls.all_results.keys():
            print("zero")
            print(cls.all_results[key])
    def test_tour1(self):
        tour1 = Tournament(90, self.runner1, self.runner3)
        medals = tour1.start()
        self.all_results.update({1: medals})
        self.assertEquals(medals[2], 'nick')
    def test_tour2(self):
        tour2 = Tournament(90, self.runner2, self.runner3)
        medals = tour2.start()
        self.all_results.update({1: medals})
        self.assertEquals(medals[2], 'nick')
    def test_tour3(self):
        tour3 = Tournament(90, self.runner1, self.runner2, self.runner3)
        medals = tour3.start()
        self.all_results.update({1: medals})
        self.assertEquals(medals[3], 'nick')

if __name__ == '__main__':
    unittest.main()
